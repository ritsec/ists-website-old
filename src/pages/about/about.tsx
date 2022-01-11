import React from "react";

import "./about.scss";
import HeroBg from "../../res/diagonal-lines.svg";

const About: React.FC = (): React.ReactElement => {
  return (
    <div className="about-container">
      <div
        className="hero mini-hero"
        style={{ backgroundImage: `linear-gradient(to bottom, rgba(18, 18, 18, 1), rgba(0, 0, 0, 0)), url(${HeroBg})` }}
      >
        <h1>About</h1>
      </div>
      <div className="content">
        <div className="card">
          <h2>General</h2>
          Each year, colleges from around the country compete for the coveted title of ISTS champion. Competitors are faced with a wide
          variety of challenges which are designed to cover as many facets of computing security, system administration, networking, and
          programming as we possibly can. These challenges include code review, architecture design, incident response, and policy writing
          -- all while defending a completely student-built infrastructure.
        </div>
        <div className="card">
          <h2>How are we different?</h2>
          From day one of competition planning, ISTS is built from the ground up by students. All of the planning, scheduling, building, and
          outreach is done by members of RITSEC. Additionally, competitor skills are put to the test by adding an external red team of
          security professionals including industry partners and passionate alumni. The red team performs offensive actions against the
          competitors during the entire competition. Notable red team members of past ISTS competitions include{" "}
          <a href="Raphael Mudge" target="_blank" rel="noreferrer">
            Raphael Mudge
          </a>{" "}
          (creator of Cobalt Strike),{" "}
          <a href="https://twitter.com/carnal0wnage" target="_blank" rel="noreferrer">
            Chris Gates
          </a>{" "}
          (carnal0wnage), and{" "}
          <a href="https://twitter.com/mubix/" target="_blank" rel="noreferrer">
            Rob Fuller
          </a>{" "}
          (Mubix).
        </div>
        <div className="card">
          <h2>Who?</h2>
          ISTS is hosted by RITSEC, the student-run computer security club at the Rochester Institute of Technology. All of the event
          planning, content creation, and day-of volunteering is done by dedicated members of RITSEC. All teams that compete at ISTS are
          composed entirely of college students. Each year, several universities around the country are invited to send a team to ISTS. RIT
          students form the remaining teams.
        </div>
      </div>
    </div>
  );
};

export default About;
