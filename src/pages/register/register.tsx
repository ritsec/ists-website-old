import React from "react";

import "./register.scss";
import HeroBg from "../../res/diagonal-lines.svg";

const Register: React.FC = (): React.ReactElement => {
  return (
    <div
      className="home register-container"
      style={{ backgroundImage: `linear-gradient(to bottom, rgba(18, 18, 18, 1), rgba(0, 0, 0, 0)), url(${HeroBg})` }}
    >
      <div>
        <h1>
          I<span style={{ display: "none" }}>o</span>STS 2022 Coming Soon...
        </h1>
      </div>
    </div>
  );
};

export default Register;
