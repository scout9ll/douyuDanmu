import React, { useEffect, useState } from "react";

function DanmuDetail({ match }) {
  const [danmu, setDanmu] = useState();
  useEffect(() => {
    getDanmu(match.params.name);
    console.log(danmu);
    console.log(match);
  }, []);
  async function getDanmu(match) {
    if (match && !match.match(/\s/g)) {
      const response = await fetch(
        `http://127.0.0.1:8000/api/leads/?message__icontains=&name__iexact=${match}&created_at__iexact=&created_at__lte=&created_at__gte=`
      );

      const data = await response.json();
      setDanmu(data);
      console.log(danmu);
    }
  }

  return (
    <table className="danmuDetail-table">
      <thead>
        <tr>
          <th>昵称</th>
          <th>等级</th>
          <th>粉丝牌</th>
          <th>粉丝等级</th>
          <th>发言内容</th>
          <th>发言时间</th>
          <th>发言房间</th>
        </tr>
      </thead>
      <tbody>
        {danmu
          ? danmu.map(danmud => (
              <tr>
                {[
                  "name",
                  "lv",
                  "bnn",
                  "bl",
                  "message",
                  "created_at",
                  "room_id"
                ].map(detail => (
                  <td>{danmud[detail]}</td>
                ))}
              </tr>
            ))
          : "loading"}
      </tbody>
    </table>
  );
}
// react中每个li给个key,可以在重新渲染DOM时,通过匹配key来优化diff,减去不必要的删除增加(例如若没key换个位置就会全部重写)
export default DanmuDetail;
