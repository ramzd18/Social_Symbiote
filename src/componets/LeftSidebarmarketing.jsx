import React from 'react'
import { Link } from 'react-router-dom';

const LeftSidebarmarketing = () => {
  return (
    <div className='left-sidebar'>
      <div className='logo'>
        <img src="./aliaslogodarksvg.svg" />
      </div>

      <Link to="/home">
        <button ><img src="./homeblack.svg" /> <span>Home</span></button>
      </Link>

      <Link to="/person">
        <button><img src="./personablack.svg" /> <span> Your personas</span></button>
      </Link>
      <Link to="/interviews">
        <button><img src="./chatblack.svg" /> <span> User interviews</span></button>
      </Link>

      <div className='active'>
        <button disabled><img src="./testingwhite.svg" /> <span> User Testing</span></button>
      </div>



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

export default LeftSidebarmarketing;