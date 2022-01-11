import React from "react";

import "./resources.scss";
import HeroBg from "../../res/diagonal-lines.svg";

const Resources: React.FC = (): React.ReactElement => {
  return (
    <div
      className="home register-container"
      style={{ backgroundImage: `linear-gradient(to bottom, rgba(18, 18, 18, 1), rgba(0, 0, 0, 0)), url(${HeroBg})` }}
    >
      <div>
        <h2>General</h2>
        <a href="http://calendar.ritsec.club" target="_blank" rel="noreferrer">
          RITSEC Calendar
        </a>
      </div>
      <div>
        <h2>Videos</h2>
        <a href="https://www.youtube.com/watch?v=4SjgMEtb27w" target="_blank" rel="noreferrer">
          Blue Linux
        </a>
        <a href="https://www.youtube.com/watch?v=hum4hzNE_j8" target="_blank" rel="noreferrer">
          Blue Windows
        </a>
        <a href="https://www.youtube.com/watch?v=w8Xs58cHcr8" target="_blank" rel="noreferrer">
          Blue Networking
        </a>
        <a href="https://www.youtube.com/watch?v=VvoDrT452Jc" target="_blank" rel="noreferrer">
          Intro to Incident Response
        </a>
        <a href="https://www.youtube.com/watch?v=HYbwn-WGWP8" target="_blank" rel="noreferrer">
          Intro to Services
        </a>
        <a href="https://www.youtube.com/watch?v=Fq__gkq9sxs" target="_blank" rel="noreferrer">
          How to Blue Team
        </a>
      </div>
    </div>
  );
};

export default Resources;
