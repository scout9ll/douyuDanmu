import React, { Component } from "react";
import ReactDOM from "react-dom";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import Danmu from "./danmu/danmuSearch";
import DanmuDetail from "./danmu/danmuDetail";
import { Provider } from "react-redux";
import store from "../store";
require("../style/App.css");
function App() {
  return (
    <Provider store={store}>
      <Router>
        <div className="App">
          <Switch>
            <Route path="/" exact component={Danmu} />
            <Route path="/Danmu" exact component={Danmu} />
            <Route path="/Danmu/:name" exact component={DanmuDetail} />
          </Switch>
        </div>
      </Router>
    </Provider>
  );
}

export default App;
