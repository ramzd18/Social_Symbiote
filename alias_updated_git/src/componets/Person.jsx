import React from 'react'
import LeftSidebarperson from './Leftsidebarperson'
import { Link } from 'react-router-dom';
import { useEffect, useState, useRef } from 'react';
import { userdata } from './Signin';
import { jwtDecode } from "jwt-decode";



function Person() {
    const [agentNames, setAgentNames] = useState([]);
    const [agentName, setAgentName] = useState('');
    const [agentAges, setAgentAges] = useState([]);
    const [agentAge, setAgentAge] = useState('');
    const [agentDescs, setAgentDescs] = useState([]);
    const [agentDesc, setAgentDesc] = useState('');
    const [agentLastInterviews, setAgentLastInterviews] = useState([]);
    const [agentLastInterview, setAgentLastInterview] = useState('');
    const [agentGenders, setAgentGenders] = useState([]);
    const [agentGender, setAgentGender] = useState('');
    const [agentJobs, setAgentJobs] = useState([]);
    const [agentJob, setAgentJob] = useState('');
    const token = sessionStorage.getItem('token');
    const isFirstRun = useRef(true);
    console.log(token)


        const decoded = jwtDecode(token);
        console.log(decoded);
        // Now you can access the user data in the decoded object


    const { user: userObject } = decoded;
    console.log(userObject);

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
        
        fetch('http://localhost:5433/getAgentDesc', {
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
            if (data.descs) {
                console.log('Multiple Descriptions:', data.descs);
                // Store the array in the state or variable
                setAgentDescs(data.descs);
                setAgentDesc('');
            } else if (data.desc) {
                console.log('Single Name:', data.desc);
                // Handle a single name separately
                setAgentDesc(data.desc);
                setAgentDescs([]);
            } else {
                console.error('Error:', data); // Log any unexpected response
            }
            // ... rest of your code
        })
        .catch((error) => console.error('Error:', error));

        fetch('http://localhost:5433/getAgentJob', {
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
            if (data.jobs) {
                console.log('Multiple Jobs:', data.jobs);
                // Store the array in the state or variable
                setAgentJobs(data.jobs);
                setAgentJob('');
            } else if (data.job) {
                console.log('Single Job:', data.job);
                // Handle a single name separately
                setAgentJob(data.desc);
                setAgentJobs([]);
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
            


        fetch('http://localhost:5433/getAgentAge', {
            method: 'POST',
            headers: {
            'Content-Type': 'application/json',
            },
            body: JSON.stringify({ email: userObject.email }),
        })
        
            .then((response) => response.json())
            .then((data) => {
                if (data.ages) {
                    console.log('Multiple Ages:', data.ages);
                    // Store the array in the state or variable
                    setAgentAges(data.ages);
                    setAgentAge('');
                } else if (data.age) {
                    console.log('Single Ages:', data.age);
                    // Handle a single name separately
                    setAgentAge(data.age);
                    setAgentAges([]);
                } else {
                    console.error('Error:', data); // Log any unexpected response
                }
                /* console.log('Agent Age:', data.age);
                setAgentAge(data.age); */
            })
            .catch((error) => console.error('Error:', error));   

            }, []);

            useEffect(() => {
                if (agentNames.length > 0) {
                    agentNames.forEach((name, index) => {
                      console.log('Name:', name);
                      fetch('http://localhost:5433/updateProfilePicture', {
                        method: 'POST',
                        headers: {
                          'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({ name: name, profile_picture: index + 1 }),
                      })
                        .then(response => response.json())
                        .then(data => {
                          console.log('Response Data:', data);
                          // Handle any UI changes or further actions if needed
                        })
                        .catch(error => {
                          console.error('Error:', error);
                        });
                    });
                  }
              }, [agentNames]);


  return (
    <>
    <section className='home container-fluid'>
   {/*<div className="logo-section "> 
    
   </div>*/}
    <div className="row">
        <div className="col-md-4">
            <LeftSidebarperson/>
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
        {/*}
        <div className="sidebarbottom">
        <li> <img src="./tool-02.png" alt="" /> Integrations</li>
        <li> <img src="./users-plus.png" alt="" />Billing</li>
        <li><img src="./help outline.png" alt="" />Support</li>
        </div>
        */}
    </div>
        {/*</div>*/}
        <div className="col-md-8 bperson">
         <div className="bperson-inner-childs">
             {/*}
           <div className="project">


           <div className="selecti">
           <select name="cars" id="cars">
                <option value="Most Recent">Most Recent</option>
                <option value="saab">Saab</option>
                <option value="mercedes">Mercedes</option>
                <option value="audi">Audi</option>
           </select>
            </div>
            
                <button>+  New Project</button>
               
            </div>
            */} 

            <div className="person">
                <Link to="/popup">
                    <button> 
                        <img src="./add.svg"/>
                        <span> New Persona</span>
                    </button>
                </Link>    
            </div>

            <div className ="container">
                {agentNames.map((name, index) => (
                    <div className="personcard" key={index}>
                    <div className="car1 d-flex">
                        <img src={`${process.env.PUBLIC_URL}/avatars/${agentGenders[index]}/${index + 1}.svg`} alt="" />  
                        <div className="car1text">
                        <h5>{name}</h5>
                        <p>{agentAges[index]} yrs - {agentJobs[index]}</p>
                        </div>
                    </div>
                    <div className="car2">
                        <p>Last Interviewed: {agentLastInterviews[index]} days ago</p>
                        <p>{agentDescs[index]} </p>
                    </div>
                    {/*<div className="car3">
                        <img src="./Group 46.png" alt="" />
                    </div>
                    */}
                    </div>
                ))}
            </div>
            {/*}
            <div className="personcard">
                <div className="car1 d-flex">
                    <img src="./Ellipse 63.png" alt="" />
                    <div className="car1text">
                    <h5>{agentName}</h5>
                    <p>{agentAge} yrs - Software Engineer</p>
                    </div>
                </div>
                <div className="car2">
                    <p>Last Interviewed: 2 days ago</p>
                    <p>A 22 year old college graduate struggling to pay<br></br> off his student debt.</p>
                </div>
                <div className="car3">
                    <img src="./Group 46.png" alt="" />
                </div>
            </div>
                */}
         </div>
           
        </div>
    {/*</div> */}
    </section>
    </>
  )
}

export default Person