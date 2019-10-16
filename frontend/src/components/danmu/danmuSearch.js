import React, { useEffect, useState } from "react";
import ReactDOM from "react-dom";
import { Link } from "react-router-dom";
function Danmu() {
  const [searchName, setSearchName] = useState("");
  const [searchMessage, setSearchMessage] = useState("");
  const [searchType, setSearchType] = useState("name");
  const [query, setQurey] = useState({});
  const [danmus, setDanmus] = useState([]);
  async function getDanmu() {
    if (
      (query.name && !query.name.match(/\s/g)) ||
      (query.message && !query.message.match(/\s/g))
    ) {
      const response = await fetch(
        `http://127.0.0.1:8000/api/leads/?message__icontains=${
          query.message
        }&name__iexact=${
          query.name
        }&created_at__iexact=&created_at__lte=&created_at__gte=`
      );

      const data = await response.json();
      data[0] ? setDanmus(data) : setDanmus(["notFound"]);
      console.log(data);
    }
  }
  useEffect(() => {
    getDanmu();
  }, [query]);
  const updateSearchName = e => {
    setSearchName(e.target.value);

    console.log(searchName);
  };
  const updateSearchMessage = e => {
    setSearchMessage(e.target.value);

    console.log(searchMessage);
  };
  const selectSearchType = e => {
    setSearchType(e.target.getAttribute("value"));

    console.log(searchType);
  };

  const getSearch = e => {
    e.preventDefault();

    setQurey({ name: searchName, message: searchMessage });
  };
  return (
    <div className="danmuSearch">
      <form action="" className="search-form" onSubmit={getSearch}>
        <div className="search-bar">
          {searchType == "name" ? (
            <input
              type="text"
              className="search-ipt name name-active"
              value={searchName}
              onChange={updateSearchName}
              placeholder="name"
            />
          ) : (
            <input
              type="text"
              className="search-ipt message message-active"
              value={searchMessage}
              onChange={updateSearchMessage}
              placeholder="messages"
            />
          )}
          <div className="select" onClick={selectSearchType}>
            <span
              value="name"
              className={`select-name  ${
                searchType == "name" ? "name-active" : null
              }`}
            >
              昵称
            </span>
            <span
              value="message"
              className={`select-message  ${
                searchType == "message" ? "message-active" : null
              }`}
            >
              内容
            </span>
          </div>
          <button className="search-button" type="submit">
            <i className="fas fa-search fa-5x" />
          </button>
        </div>
        <ul className="suggestions">
          {danmus[0] == "notFound" ? (
            <li>木有找到</li>
          ) : (
            danmus.map(danmu => (
              <li key={danmu.cid}>
                <span className="name">
                  <Link to={`/danmu/${danmu.name}`}> {danmu.name}</Link>
                </span>
                <span className="name">{danmu.message}</span>
              </li>
            ))
          )}
        </ul>
      </form>
    </div>
  );
}
export default Danmu;
