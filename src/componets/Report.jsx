import React from 'react'
import { Link } from 'react-router-dom';
import LeftSidebarinterviews from './Leftsidebarinterviews'
import { jwtDecode } from "jwt-decode";
import { useEffect, useState } from 'react';
import ProgressCircle from './ProgressCircle';

function Report() {
    const selectedAgentName = sessionStorage.getItem('selectedAgentName');
    const selectedAgentPic = sessionStorage.getItem('selectedAgentPic');
    const selectedAgentGender = sessionStorage.getItem('selectedAgentGender');
    const selectedAgentAge = sessionStorage.getItem('selectedAgentAge');
    const selectedAgentJob = sessionStorage.getItem('selectedAgentJob');
    const [reportFinal, setReportFinal] = useState({})

    const token = sessionStorage.getItem('token');
    const decoded = jwtDecode(token);
    const { user: userObject } = decoded;
    console.log(userObject);

    useEffect(() => {
        fetch(`https://alias-node-9851227f2446.herokuapp.com/get-report`, {
            method: 'POST',
            headers: {
            'Content-Type': 'application/json',
            },
            body: JSON.stringify({ name: selectedAgentName, personEmail: userObject.email }), // Ensure the body is an object
        })
        .then((response) => response.json()) // Try parsing response as JSON
        .then((data) => {
            setReportFinal(data)
        })
        .catch((error) => console.error('Error:', error));
    }, []);

    console.log(reportFinal)
    const dictionaryLength = Object.keys(reportFinal).length;
    console.log(dictionaryLength)


return (
    <section className='home container-fluid'>
        <div className="row">
        <div className="col-md-4">
          <LeftSidebarinterviews/>
        </div>  
        </div>
        <div className="col-md-8 big">
            <div className="big-inner-child">
                <Link to="/interviews">
                    <button className="backarrowreport"> <img src="./Arrow-Left.svg" /> </button>
                </Link>
                <div className="big-inner-reports">
                    <div className="int">
                        <div className="intimg">
                            {/* <img src={`${process.env.PUBLIC_URL}/avatars/${selectedAgentGender}/${selectedAgentPic}.svg`} alt="" /> */}
                            <img src={`${process.env.PUBLIC_URL}/avatars/M/1.svg`} alt="" />
                        </div>
                        <div className="inttext">
                            <h4>{selectedAgentName}</h4>
                            {/* <h4>Chris Lopez</h4> */}
                            <p>{selectedAgentAge} yrs - {selectedAgentJob}</p>
                            {/* <p>20 yrs - Software Engineer</p> */}
                        </div>
                    </div>
                    <div className="subhead">
                        <h5>About me</h5>
                        {/* <p>I am a Gen Z recent college graduate living in New York City. I work in software engineering and earn above $200,000/yr. I’m originally from Chicago and attended Cornell.</p> */}
                        {dictionaryLength > 0 ? (
                        <p>{reportFinal["Tell me about yourself"]}</p>
                        ) : (
                        <p>No report available</p>
                        )}
                    </div>
                    <div className="subheadtwo">
                        <div>
                            <h5>Interests & hobbies</h5>
                            {dictionaryLength > 0 ? (
                            <p>{reportFinal["Interests & hobbies"]}</p>
                            ) : (
                            <p>No report available</p>
                            )}
                            {/* <ul>
                                <li>Playing video games since a child</li>
                                <li>Stock trading with college friends</li>
                                <li>Testing new products after buying first iPhone</li>
                            </ul> */}
                        </div>
                        
                        <div>
                            <h5>Personality traits</h5>
                            {dictionaryLength > 0 ? (
                            <p>{reportFinal["Personality traits"]}</p>
                            ) : (
                            <p>No report available</p>
                            )}
                            {/* <ul>
                                <li>Introverted</li>
                                <li>Apprehensive to new experiences</li>
                                <li>Compassionate</li>
                            </ul> */}
                        </div> 

                    </div>
                    <div className="subheadthree">
                        <h5>Pain points</h5>
                        {/* <p>I am a Gen Z recent college graduate living in New York City. I work in software engineering and earn above $200,000/yr. I’m originally from Chicago and attended Cornell.</p> */}
                        {dictionaryLength > 0 ? (
                        <p>{reportFinal['Thoughts on problem']}</p>
                        ) : (
                        <p>No report available</p>
                        )}
                    </div>

                    <div className="subheadfour">
                        <h5>Analysis of your competitors</h5>
                        {/* <p>I am a Gen Z recent college graduate living in New York City. I work in software engineering and earn above $200,000/yr. I’m originally from Chicago and attended Cornell.</p> */}
                        {dictionaryLength > 0 ? (
                        <p>{reportFinal["Competitors"]}</p>
                        ) : (
                        <p>No report available</p>
                        )}
                    </div>


                    <div className="subheadfive">
                        <h5>Thoughts on your product</h5>
                        {/* <p>I am a Gen Z recent college graduate living in New York City. I work in software engineering and earn above $200,000/yr. I’m originally from Chicago and attended Cornell.</p> */}
                        {dictionaryLength > 0 ? (
                        <p>{reportFinal["Thoughts on product"]}</p>
                        ) : (
                        <p>No report available</p>
                        )}
                    </div>

                    <div className="subheadsix">
                        <div>
                            <h5>Questions & concerns</h5>
                            <ul>
                                <li>Playing video games since a child</li>
                                <li>Stock trading with college friends</li>
                                <li>Testing new products after buying first iPhone</li>
                            </ul>
                        </div>
                        <div>
                            <h5>&nbsp;</h5>
                            <ul>
                                <li>Introverted</li>
                                <li>Apprehensive to new experiences</li>
                                <li>Compassionate</li>
                            </ul>
                        </div>
                    </div>

                    <div className="sum">
                        <h5>Summary</h5>
                        {dictionaryLength > 0 ? (
                            <div>
                            {reportFinal["Scores"].map((score, index) => (
                                <div key={index} className="progress-circle">
                                    {score.toFixed(2)}
                                </div>
                            ))}
                        </div>
                    ) : (
                        <p>No report available</p>
                    )}
                       
                    </div>

                    <Link to="/interface" className="link-no-underline"> 
                    <div className='reportbutton'>
                            <button>Open Chat</button>
                    </div>        
                    </Link>
                    
                </div>    
            </div>
        </div>
    </section>
)

}

export default Report