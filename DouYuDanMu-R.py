import re
import time
import datetime
import socket
import logging
import threading
import sqlite3

# 配置日志
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class DyDanmu:
    def __init__(self, room_id):
        self.room_id = room_id
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostbyname("openbarrage.douyutv.com")
        port = 8601
        self.client.connect((host, port))

    def send_msg(self, msg):
        # 发送数据
        msg = msg + '\0'  # 数据以'\0'结尾
        msg = msg.encode('utf-8')  # 使用utf-8编码
        length = len(msg) + 8  # 消息长度
        code = 689  # 消息类型
        # 消息头部：消息长度+消息长度+消息类型+加密字段(默认为0)+保留字段(默认为0)
        head = int.to_bytes(length, 4, 'little') + int.to_bytes(length,
                                                                4, 'little') + int.to_bytes(code, 4, 'little')
        # 发送头部部分
        self.client.send(head)
        # 发送数据部分
        sent = 0
        while sent < len(msg):
            n = self.client.send(msg[sent:])  # 返回已发送的数据长度
            sent = sent + n

    def login(self):
        # 登录授权
        login_msg = "type@=loginreq/roomid@={}/".format(self.room_id)
        self.send_msg(login_msg)
        # 加入房间
        join_msg = "type@=joingroup/rid@={}/gid@=-9999/".format(self.room_id)
        self.send_msg(join_msg)
        logging.info("Succeed in logging in.")

    def get_danmu(self):
        # 获取弹幕和礼物信息
        sql_conn = sqlite3.connect('db2.sqlite3')
        c = sql_conn.cursor()
        while True:
            try:
                data = self.client.recv(2048)
                data = data.decode(encoding='utf-8', errors='ignore')
                if re.search('type@=chatmsg', data):
                    pattern1 = re.compile(
                        'nn@=([^@]*?)/txt@=([^@]*?)/cid@=([^@]*?)/.*?/level@=([^@]*?)/.*?/bnn@=([^@]*?)/bl@=([^@]*?)/')
                    danmu = re.findall(pattern1, data)[0]
                    print(danmu)

                    data = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    # 导入数据库
                    c.execute(
                        "INSERT INTO leads_lead (name,lv,message,bnn,bl,created_at,cid,room_id_id)"
                        "VALUES ('%s',' %s', '%s', '%s', '%s','%s','%s','%s')"
                        % (danmu[0], danmu[3], danmu[1], danmu[4], danmu[5], data, danmu[2], roomID))
                    sql_conn.commit()

            except KeyError:
                pass
            except Exception as e:
                logging.info(e)

    def keep_live(self):
        # 用于维持和后台间的心跳
        while True:
            keep_msg = "type@=mrkl/"  # 新版协议心跳消息
            self.send_msg(keep_msg)
            time.sleep(40)
            logging.info("Keep live...")

    def main(self):
        self.login()

        p1 = threading.Thread(target=self.get_danmu)
        p2 = threading.Thread(target=self.keep_live)
        p1.start()
        p2.start()


if __name__ == '__main__':
    # sql_conn = sqlite3.connect('db2.sqlite3')
    # sql_conn.close()
    roomID = input('请输入房间ID： ')
    dy = DyDanmu(roomID)
    dy.main()
