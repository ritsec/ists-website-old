import React from "react";

import "./home.scss";
import HeroBg from "../../res/diagonal-lines.svg";

const Home: React.FC = (): React.ReactElement => {
  return (
    <div className="home-container">
      <div
        className="hero"
        style={{ backgroundImage: `linear-gradient(to bottom, rgba(18, 18, 18, 1), rgba(0, 0, 0, 0)), url(${HeroBg})` }}
      >
        <h1>ISTS</h1>
        <h3>
          RITSEC's Information Security Talent Search (ISTS) competition is an annual three-day cyber attack/ defend competition hosted at
          the Rochester Institute of Technology by RITSEC.
        </h3>
      </div>
    </div>
  );
};

export default Home;
