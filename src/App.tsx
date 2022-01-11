import React, { useState } from "react";
import { Route, Switch, useLocation } from "react-router-dom";
import { TransitionGroup, CSSTransition } from "react-transition-group";

import Nav from "./components/nav/nav";
import Home from "./pages/home/home";
import About from "./pages/about/about";
import Resources from "./pages/resources/resources";
import Register from "./pages/register/register";

import "./App.scss";
import Sidebar from "./components/sidebar/sidebar";

const App: React.FC = (): React.ReactElement => {
  const location = useLocation();
  const [isSidebarOpen, setIsSidebarOpen] = useState(false);
  const [cachedHref, setCachedHref] = useState("");

  const openSidebar = () => {
    setIsSidebarOpen(!isSidebarOpen);
  };

  if (cachedHref !== window.location.href) {
    setIsSidebarOpen(false);
    setCachedHref(window.location.href);
  }

  return (
    <div className="app-container">
      <Nav openSidebar={openSidebar} isSidebarOpen={isSidebarOpen} />
      <TransitionGroup>
        <CSSTransition timeout={300} classNames="fade" key={location.key}>
          <Switch>
            <Route path="/about" component={About} />
            <Route path="/resources" component={Resources} />
            <Route path="/register" component={Register} />
            <Route path="/" component={Home} />
          </Switch>
        </CSSTransition>
      </TransitionGroup>
      <Sidebar isOpen={isSidebarOpen} />
    </div>
  );
};

export default App;
