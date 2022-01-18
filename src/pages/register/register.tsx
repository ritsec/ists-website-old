import React from "react";

import "./register.scss";
import HeroBg from "../../res/diagonal-lines.svg";

const Register: React.FC = (): React.ReactElement => {
  return (
    <div
      className="home register-container"
      style={{ backgroundImage: `linear-gradient(to bottom, rgba(18, 18, 18, 1), rgba(0, 0, 0, 0)), url(${HeroBg})` }}
    >
      <div className="info">
        <h1>ISTS 2022</h1>
        <h3>March 4th-6th 2022 @ RIT</h3>
        <p>
          <em>Note: Final decisions will be made on modality by end of February</em>
        </p>
      </div>
      <div>
        <h2>Signups</h2>
        <a href="https://forms.gle/VhQZPUFQutKwrHG5A" target="_blank" rel="noreferrer">
          Blue Team (Non-RIT)
        </a>
        <a href="https://forms.gle/PRewEH76m1mLQGHA8" target="_blank" rel="noreferrer">
          Blue Team (RIT)
        </a>
        <a href="https://forms.gle/pnsxuD6kA2J4WxQY7" target="_blank" rel="noreferrer">
          White Team (RIT)
        </a>
      </div>
    </div>
  );
};

export default Register;
