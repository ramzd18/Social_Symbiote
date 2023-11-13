import React from 'react'

function Invite() {
  return (
    <>
      <div className="container-fluid">
        <div className="workplace pd">
            <img src="./aliaslogodark 1.png" alt="" srcset="" />
            <div className="twoc text-center">
                <div className="lc"></div>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                <div className="fc"></div>
            </div>
            <div className="step">
            <p className='text-center step pb-5'>Step 2 of 2</p>
            <h2>Invite your teammates</h2>
            <h5>Customer insights, company wide</h5>
            </div>
            <div className="invite-form mt-5">
              <div className="innerbu">
                <button>name@company.com</button>
                <button>name@company.com</button>
                <button>name@company.com</button>
                <button>name@company.com</button>
                <button>name@company.com</button><br></br>
                <div className="plus">
                <span className=''><i className="fa-solid fa-plus"></i>Add teammate</span>
                </div>
              </div>
            </div>
            <div className="invite-form signin">
                <button>Send Invites</button>
                <h6 className='text-center pt-5 skip'>Skip this step</h6>
            </div>
            </div>
            </div>
    </>
  )
}

export default Invite