import React from 'react'

function Workplace() {
  return (
    <>
    <div className="container-fluid">
        <div className="workplace pd">
            <img src="./aliaslogodark 1.png" alt="" srcset="" />
            <div className="twoc text-center">
                <div className="fc"></div>
                <div className="lc"></div>
            </div>
            <div className="step">
            <p className='text-center step pb-5'>Step 1 of 2</p>
            <h2>Create your workspace</h2>
            <h5>A secure playground for your interviews</h5>
            <div className="work-form ">
            <label htmlFor="Full Name">Company Name</label><br></br>
            <input type="email" placeholder='e.g Alias '/><br></br>

            <label for="cars">I'm a</label><br></br>
<select name="Select a Role" id="Select a Role">
  <option value="volvo">Select a Role</option>
  <option value="saab">Maneger</option>
  <option value="mercedes">Ceo</option>
  <option value="audi">Empoloye</option>
</select>

<label for="cars">My Company Has</label><br></br>
<select name="Select a Role" id="Select a Role">
  <option value="volvo">Select Team Size</option>
  <option value="saab">4</option>
  <option value="mercedes">6</option>
  <option value="audi">10</option>
</select>
<div className="signin">
                <button>Create Workspace</button>
            </div>
            </div>
            </div>
        </div>
    </div>
    </>
  )
}

export default Workplace