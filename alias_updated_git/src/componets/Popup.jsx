import React from 'react'
import Leftsidebarperson from './Leftsidebarperson'
import { Link } from 'react-router-dom';
import { useEffect, useState } from 'react';
import { jwtDecode } from "jwt-decode";
import CircularProgress from '@mui/material/CircularProgress';


function Popup() {
  const [age, setAge] = useState('');
  const [occupation, setOccupation] = useState('');
  const [description, setDescription] = useState('');
  const [isDisabled, setIsDisabled] = useState(false);
  const [isLoading, setLoading] = useState(false); // Default loading state is true
  const token = sessionStorage.getItem('token');
  const decoded = jwtDecode(token);
  const { user: userObject } = decoded;
  const email = userObject.email;


  const clearInformation = () => {
    setAge('');
    setOccupation('');
    setDescription('');
  };

  // dont create new row with data in database with passed in info - call checkrows, if rowCount < 3 then work with Ram on api
  const handleNewPersona = () => {

    if (age.trim() === '' || occupation.trim() === '' || description.trim() === '') {
      // If any field is empty, prevent the new persona action
      alert('Please fill in all the fields to create a new persona.');
      return;
    }

    setLoading(true);

    fetch(`http://localhost:5433/check-rows?personEmail=${email}`)
      .then(response => response.json())
      .then(data => {
        const rowCount = data.rowCount; // received row count from the API
        console.log('Row count:', rowCount);

        if (rowCount < 3) {
          setLoading(true);
          const response = fetch(`http://127.0.0.1:5000/create_agent?email=${email}&description=${description}&age=${age}&job=${occupation}`);
          try {
            const data = response.text();
            console.log('Response:', data);
          }
          catch (error) {
            console.error('Error creating agent:', error);
          } finally {
            setLoading(false); // Set loading state to false after receiving a response
          }
          // fetch('http://localhost:5433/add-persona', {
          //   method: 'POST',
          //   headers: {
          //     'Content-Type': 'application/json',
          //   },
          //   body: JSON.stringify({
          //     age: age,
          //     occupation: occupation,
          //     description: description,
          //     personEmail: email,
          //   }),
          // })
          //   .then(response => {
          //     if (response.ok) {
          //       console.log('New persona added successfully');
          //       // Ensure loading indicator is turned off after completion
          //       setLoading(false);
          //     } else {
          //       console.error('Failed to add new persona');
          //       setLoading(false);
          //     }
          //   })
          //   .catch(error => {
          //     console.error('Error while adding new persona:', error);
          //     setLoading(false);
          //   });
        } else {
          setIsDisabled(true);
          setLoading(false); // Turn off the loading indicator if not adding a new persona
        }
      })
      .catch(error => {
        console.error('Error while checking row count:', error);
        setLoading(false);
      });
      };    
      
  return (
  

  <section className='home container-fluid'>
   
   {/*<div className="logo-section ">
    
  </div> */}
    <div className="row">
        <div className="col-md-4">
          <Leftsidebarperson/>
        </div>
        {/*}  
        <div className="left-sidebar">
        <div className="sidebartop">
        <div className="logo">
   <img src="./aliaslogodarksvg.svg" alt="" srcset="" />
   </div>
   
        <li className=''> <img src="./homeblack.svg" alt="" />Home</li>
        
        <li className='active'><img src="./personawhite.svg" alt="" />Your personas</li>
        <li> <img src="./chatblack.svg" alt="" /> User interviews</li>
        </div>

        <div className="sidebarbottom">
        <li> <img src="./tool-02.png" alt="" /> Integrations</li>
        <li> <img src="./users-plus.png" alt="" />Billing</li>
        <li><img src="./help outline.png" alt="" />Support</li>
        </div>
        */}

    </div>
        {/*</div> */}
        <div className="col-md-8 big">
         <div className="big-inner-childs-popup">
            <Link to="/person">
              <button className="backarrow"> <img src= "./Arrow-Left.svg" /> </button>
            </Link>
          <div className="personcardpopup">
            <h4>Create your persona</h4>
          <div className="popup">
            <div className="lb1">
              <label htmlFor="Full Name">Age:</label><br></br>
                <input
                  type="text"
                  placeholder="e.g 21, 45-60"
                  value={age}
                  onChange={(e) => setAge(e.target.value)}
                />
            </div>
                    <div className="lb2">
                      <label htmlFor="Full Name">Occupation:</label><br></br>
                      <input
                        type="text"
                        placeholder="e.g Software Engineer"
                        value={occupation}
                        onChange={(e) => setOccupation(e.target.value)}
                      />
                    </div> 

                                
        </div>
        <div className="mtextarea pt-5">
                <label htmlFor="Description">Describe your target customer:</label><br></br>
                <textarea
                  cols="80"
                  rows="5"
                  value={description}
                  onChange={(e) => setDescription(e.target.value)}
                ></textarea>
        </div>  

        <div className='popupline'></div>
        <div>
          {isLoading ? (
            <CircularProgress />
          ) : (
          <div className="mbuttonarea text-center">
              <Link to={age.trim() !== '' && occupation.trim() !== '' && description.trim() !== '' ? "/person" : "#"}>
                <button className='customButton' disabled={isDisabled} title={isDisabled ? 'Max personas created' : undefined} onClick={handleNewPersona} >New Persona</button>
              </Link>
              <button onClick={clearInformation}>Clear Information</button>
          </div>
        )}
        </div>  
         </div>
         </div>
           
        </div>
    </section>
  )
}

export default Popup