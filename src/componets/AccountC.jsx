import React, { useEffect, useState } from 'react';
import { jwtDecode } from "jwt-decode";
import { Link } from 'react-router-dom';

let userdata = {};

function AccountC() {
  const [user, setUser] = useState({});
  const [userExists, setUserExists] = useState(false);

  function handleCallbackResponse(response) {
    /* console.log(response.credential); */
    var userObject = jwtDecode(response.credential);
    /* console.log(userObject); */
    setUser(userObject);
    /* console.log(user); */
    console.log(userObject);
    userdata = userObject;
    fetch('http://localhost:5433/createUser', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(
        {
          given_name: userObject.given_name,
          family_name: userObject.family_name,
          email: userObject.email,
        }  
      ),

    })

      .then((response) => {
        if (response.ok) {
          console.log('User info sent to the backend');
          // Success handling logic
        } else if (response.status === 400) {
          return response.json().then(data => {
            console.error('Error:', data);
            setUserExists(true);
            // Display an error message to the user
            // For example:
            // alert(data);
          });
        } else {
          console.error('Failed to send user info to the backend');
          // Other failure handling logic
        }
      })
      .catch((error) => {
        console.error('Error:', error);
        console.error('Error Message:', error.message);
      }); 
    

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

  useEffect(() => {
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

  const hasNameAndEmail = user && user.given_name && user.family_name && user.email;

  return (
    <>
    <div className="container-fluid">
        <div className="accountc">
        
        <div className="row">
            <div className="col-md-8 pd account">
            <img src="./aliaslogodarksvg.svg" alt="" />
            <h2>Create your Alias account</h2>
            <div id="gbutton">
                <button><img src="./google.png" alt="" /> <span>Sign up with Google</span></button> 
            </div>

            <div className="signinbeta">
              <h6>Already have an account? Sign in <Link to="/signin" style={{ color: 'black' }} >here</Link>.</h6>
            </div>  

            <div className="signinbetanew">
              {hasNameAndEmail ? (
                <Link to="/home">
                  <button disabled={userExists}>Create Account</button>
                </Link>
              ) : (
                <button disabled={userExists}>Create Account</button>
              )}
              {userExists && (
                <div className="error-message">Account already exists, please sign in.</div>
              )}
            </div>
          {/*
           <div className="or">
           <p>&nbsp; &nbsp; Or, sign up with email &nbsp; &nbsp; </p>
           <div className="form">
            <label htmlFor="Full Name">Full Name</label><br></br>
            <input type="text" placeholder='e.g Example Name'/><br></br>

            <label htmlFor="Full Name">Email Address</label><br></br>
            <input type="email" placeholder='e.g example@company.com'/><br></br>

            <label htmlFor="Full Name">Password</label><br></br>
            <input type="password" placeholder='Set Password'/>

            <div className="signin">
                <button>Create Account</button>
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

export default AccountC;
export { userdata };