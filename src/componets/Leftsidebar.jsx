import React from 'react'
import { Link } from 'react-router-dom';

const LeftSidebar = () => {
  return (
    <div className='left-sidebar'>
      <div className='logo'>
        <img src="./aliaslogodarksvg.svg" />
      </div>

      <div className='active'>
        <button disabled><img src="./homewhite.svg" /> <span>Home</span></button>
      </div>
      <Link to="/person">
        <button><img src="./personablack.svg" /> <span> Your personas</span></button>
      </Link>
      <Link to="/interviews">
        <button><img src="./chatblack.svg" /> <span> User interviews</span></button>
      </Link>
      <Link to="/testing">
        <button><img src="./chatblack.svg" /> <span> User Testing</span></button>
      </Link>



      {/*  <div className="left-sidebar">
          <div className="sidebartop">
          <div className="logo">
    <img src="./aliaslogodark 1.png" alt="" srcset="" />
    </div>
          <li> <img src="./Home.png" alt="" />Home</li>
          <li><img src="./supervisor account.png" alt="" />Your personas</li>
          <li> <img src="./chat.png" alt="" /> User interviews</li>
          </div>
          <div className="sidebarbottom">
          <li> <img src="./tool-02.png" alt="" /> Integrations</li>
          <li> <img src="./users-plus.png" alt="" />Billing</li>
          <li><img src="./help outline.png" alt="" />Support</li>
          </div>

      </div>
      */}
    </div>
  )
}

export default LeftSidebar;