import sqlite3
import datetime

data = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
conn = sqlite3.connect('db2.sqlite3')
c = conn.cursor()

c.execute("INSERT INTO leads_lead (name,lv,message,bnn,bl,created_at)VALUES ('测试者', 1, '????', '测试者', '0','%s')" % data)
conn.commit()
conn.close()
