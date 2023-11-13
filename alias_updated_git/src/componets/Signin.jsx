import React, { useEffect, useState } from 'react';
import { jwtDecode } from "jwt-decode";
import { Link } from 'react-router-dom';
import useUserData from './userdata';



let userdata = {};

function Signin() {
  const [isUser, setIsUser] = useState(false);;

  
  function handleCallbackResponse(response) {
    /*c onsole.log(response.credential); */
    var userObject = jwtDecode(response.credential);
    /*console.log(userObject); */
    console.log(userObject.email); 

    fetch(`http://localhost:5433/checkUser?email=${userObject.email}`) // replace with the actual email
      .then((response) => response.json()) // Try parsing response as JSON
        /* if (response.ok) {
          setIsUser(true); // Set state to allow the button to be clickable
          localStorage.setItem('loggedIn', 'true'); // Store logged-in status in local storage
          userdata = userObject;

        } else {
          setIsUser(false); // Set state to disable the button
          localStorage.setItem('loggedIn', 'false'); // Store logged-in status in local storage
        }
            })
  
        */

      .then((data) => {
        console.log('Data:', data);
        if (data.token) {
          console.log('Token:', data.token); // Log the token received
          localStorage.setItem('loggedIn', 'true'); // Store logged-in status in local storage
          sessionStorage.setItem('token', data.token); // Store the token in session storage
          // Further use the token as needed
        } else {
          console.error('No token received');
        }
      })

      .catch((error) => {
        console.error('Error:', error);
      });
 
  
  }

  console.log(userdata);

  useEffect(() => {

    const loggedInStatus = localStorage.getItem('loggedIn');
    setIsUser(loggedInStatus === 'true');

    /* global google */
    google.accounts.id.initialize({
      client_id: "822420183545-p950fdql2o6ls85egkd47gtf4a6tujcc.apps.googleusercontent.com",
      callback: handleCallbackResponse
    })

    google.accounts.id.renderButton(
      document.getElementById("gbutton"),
      {theme: "outline", size: "large", innerWidth: "400px"}
    )

  }, []);
  

  return (
    <>
    <div className="container-fluid">
        <div className="accountc">
        
        <div className="row">
            <div className="col-md-8 pd account">
            <img src="./aliaslogodarksvg.svg" alt="" />
            <h2>Sign in to your Alias account</h2>
            <div id="gbutton">
                <button><img src="./google.png" alt="" /> <span>Sign in with Google</span></button>
                
            </div>
            
            <div className="signinbeta">
              <h6>By signing in, you agree to our Beta Test policy.</h6>
            </div>  


            <div className="signinbetanew">
              
              <Link to={isUser ? '/home' : '#'}>
                <button disabled={!isUser}>Sign in</button>
              </Link>  
            </div>


            {/* 
            <div className="or">
            <p>&nbsp; &nbsp; Or, sign up with email &nbsp; &nbsp; </p>
            <div className="form">
              <label htmlFor="Full Name">Email Address</label><br></br>
              <input type="email" placeholder='e.g example@company.com'/><br></br>

              <label htmlFor="Full Name">Password</label><br></br>
              <input type="password" placeholder='Set Password'/>
              <div className="signin">
                  <button>Sign in</button>
              </div>
              <h6>Already have an account? Sign in</h6>
            </div>

            </div>
            */}
              </div>
              <div className="col-md-4 bluebg">
              </div>
        </div>
        </div>
    </div>
    </>
  )
}

export default Signin;
export { userdata };
