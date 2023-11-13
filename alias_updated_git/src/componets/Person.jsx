import React from 'react'
import LeftSidebarperson from './Leftsidebarperson'
import { Link } from 'react-router-dom';
import { useEffect, useState } from 'react';
import { userdata } from './Signin';
import { jwtDecode } from "jwt-decode";



function Person() {
    const [agentNames, setAgentNames] = useState([]);
    const [agentName, setAgentName] = useState('');
    const [agentAges, setAgentAges] = useState([]);
    const [agentAge, setAgentAge] = useState('');
    const token = sessionStorage.getItem('token');
    console.log(token)


        const decoded = jwtDecode(token);
        console.log(decoded);
        // Now you can access the user data in the decoded object


    const { user: userObject } = decoded;
    console.log(userObject);

    useEffect(() => {

        fetch('http://localhost:5432/getAgentName', {
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
        
                
        fetch('http://localhost:5432/getAgentAge', {
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
        <div className="col-md-8 big">
         <div className="big-inner-childs">
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
                        <img src={`${process.env.PUBLIC_URL}/avatars/M/${index + 1}.svg`} alt="" />  
                        <div className="car1text">
                        <h5>{name}</h5>
                        <p>{agentAges[index]} yrs - Software Engineer</p>
                        </div>
                    </div>
                    <div className="car2">
                        <p>Last Interviewed: 2 days ago</p>
                        <p>A 22 year old college graduate struggling to pay off his student debt. </p>
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