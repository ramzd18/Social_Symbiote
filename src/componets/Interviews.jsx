import React from 'react'
import Leftsidebar from './Leftsidebar'
import LeftSidebarinterviews from './Leftsidebarinterviews'
import { useEffect, useState } from 'react';
import { jwtDecode } from "jwt-decode";
import { Link } from 'react-router-dom';

function Interviews() {
    const [agentNames, setAgentNames] = useState([]);
    const [agentName, setAgentName] = useState('');
    const [agentPics, setAgentPics] = useState([]);
    const [agentPic, setAgentPic] = useState('');
    const [agentGenders, setAgentGenders] = useState([]);
    const [agentGender, setAgentGender] = useState('');
    const [agentLastInterviews, setAgentLastInterviews] = useState([]);
    const [agentLastInterview, setAgentLastInterview] = useState('');


    const token = sessionStorage.getItem('token');
    const decoded = jwtDecode(token);
    const { user: userObject } = decoded;
    console.log(userObject);

    const handleInterviewClick = (name) => {
        // Handle saving the name when the button is clicked
        console.log(`Interview button clicked for ${name}`);
        sessionStorage.setItem('selectedAgentName', name);
        sessionStorage.setItem('selectedAgentGender', agentGenders[agentNames.indexOf(name)]);
        sessionStorage.setItem('selectedAgentPic', agentPics[agentNames.indexOf(name)]);
        console.log('selectedAgentName', sessionStorage.getItem('selectedAgentName'));
        console.log(sessionStorage.getItem('selectedAgentGender'));
        console.log(sessionStorage.getItem('selectedAgentPic'));
        // Further actions to save the name or navigate to a different page with this data
      };

    useEffect(() => {

        fetch('http://localhost:5433/getAgentName', {
            method: 'POST',
            headers: {
            'Content-Type': 'application/json',
            },
            body: JSON.stringify({ email: userObject.email }), // Ensure the body is an object
        })
        .then((response) => response.json()) // Try parsing response as JSON
        .then((data) => {
            {/* console.log('Response:', data.name); // Log the full response
            setAgentName(data.name);
            */}
            if (data.names) {
                console.log('Multiple Names:', data.names);
                // Store the array in the state or variable
                setAgentNames(data.names);
                setAgentName('');
            } else if (data.name) {
                console.log('Single Name:', data.name);
                // Handle a single name separately
                setAgentName(data.name);
                setAgentNames([]);
            } else {
                console.error('Error:', data); // Log any unexpected response
            }
            // ... rest of your code
        })
        .catch((error) => console.error('Error:', error));

        fetch('http://localhost:5433/getAgentPic', {
            method: 'POST',
            headers: {
            'Content-Type': 'application/json',
            },
            body: JSON.stringify({ email: userObject.email }), // Ensure the body is an object
        })
        .then((response) => response.json()) // Try parsing response as JSON
        .then((data) => {
            {/* console.log('Response:', data.name); // Log the full response
            setAgentName(data.name);
            */}
            if (data.pics) {
                console.log('Multiple pics:', data.pics);
                // Store the array in the state or variable
                setAgentPics(data.pics);
                setAgentPic('');
            } else if (data.pic) {
                console.log('Single pic:', data.pic);
                // Handle a single name separately
                setAgentPic(data.pic);
                setAgentPics([]);
            } else {
                console.error('Error:', data); // Log any unexpected response
            }
            // ... rest of your code
        })
        .catch((error) => console.error('Error:', error));

        fetch('http://localhost:5433/getAgentGender', {
            method: 'POST',
            headers: {
            'Content-Type': 'application/json',
            },
            body: JSON.stringify({ email: userObject.email }), // Ensure the body is an object
        })
        .then((response) => response.json()) // Try parsing response as JSON
        .then((data) => {
            {/* console.log('Response:', data.name); // Log the full response
            setAgentName(data.name);
            */}
            if (data.genders) {
                console.log('Multiple Genders:', data.genders);
                // Store the array in the state or variable
                setAgentGenders(data.genders);
                setAgentGender('');
            } else if (data.gender) {
                console.log('Single Gender:', data.gender);
                // Handle a single name separately
                setAgentGender(data.gender);
                setAgentGenders([]);
            } else {
                console.error('Error:', data); // Log any unexpected response
            }
            // ... rest of your code
        })
        .catch((error) => console.error('Error:', error));


        fetch('http://localhost:5433/getAgentLastInterview', {
            method: 'POST',
            headers: {
            'Content-Type': 'application/json',
            },
            body: JSON.stringify({ email: userObject.email }), // Ensure the body is an object
        })
        .then((response) => response.json()) // Try parsing response as JSON
        .then((data) => {
            {/* console.log('Response:', data.name); // Log the full response
            setAgentName(data.name);
            */}
            if (data.days) {
                console.log('Multiple Interviews:', data.days);
                // Store the array in the state or variable
                setAgentLastInterviews(data.days);
                setAgentLastInterview('');
            } else if (data.day) {
                console.log('Single Interview:', data.day);
                // Handle a single name separately
                setAgentLastInterview(data.day);
                setAgentLastInterviews([]);
            } else {
                console.error('Error:', data); // Log any unexpected response
            }
            // ... rest of your code
        })
        .catch((error) => console.error('Error:', error));
    }, []);
  return (
    <>
    <section className='home container-fluid'>
   {/*<div className="logo-section "> </div> */}
    
    <div className="row">
        <div className="col-md-4">
          <LeftSidebarinterviews/>
        </div>  
        {/*}
    <div className="left-sidebar">
        <div className="sidebartop">
        <div className="logo">
   <img src="./aliaslogodarksvg.svg" alt="" srcset="" />
   </div>
   
        <li className=''> <img src="./homeblack.svg" alt="" />Home</li>
         
        <li><img src="./personablack.svg" alt="" />Your personas</li>
        <li className='active'> <img src="./chatwhite.svg" alt="" /> User interviews</li>
        </div>
        {/*}
        <div className="sidebarbottom">
        <li> <img src="./tool-02.png" alt="" /> Integrations</li>
        <li> <img src="./users-plus.png" alt="" />Billing</li>
        <li><img src="./help outline.png" alt="" />Support</li>
        </div>
        */}
    </div>
        <div className="col-md-8 big">
         <div className="big-inner-child">
            <h2 className='pb-5'>Your Interviews</h2>
         <div className="big-inner-interviews">
            <div className="int">
            <h4>Recent Interviews</h4>
            
            {agentNames.map((name, index) => (
                    <div className="interviewtext" key={index}>
                        <div className="innerinterviewtext">
                            <div className="interimg">
                                <img src={`${process.env.PUBLIC_URL}/avatars/${agentGenders[index]}/${agentPics[index]}.svg`} alt="" />
                            </div>
                            <div className="intertext">
                                <p>User Interview with {name}</p>
                                <p> Chat with {name} today.</p>
                                
                                {/* <p>Last Interviewed: {agentLastInterviews[index]} days ago</p> */}
                            </div>
                        </div>
                        <Link to="/interface" onClick={() => handleInterviewClick(name)}>
                            <button>Interview</button>
                        </Link>
                    </div>
                ))}
             
         </div>  
         <div className="interviewline"> </div>  
         {/*}
         <div className="clear">
            <button>Clear Interviews</button>
         </div>   
            */}
         </div>

         </div>
        </div>       
    </section></>
  )
}

export default Interviews