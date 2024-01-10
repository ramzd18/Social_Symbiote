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

    const getMetricName = (index) => {
        const metricNames = ['Usability', 'Value Proposition', 'Likelihood to Recommend'];
        return metricNames[index] || '';
      };

    const canParseJSON = (str) => {
        try {
            JSON.parse(str);
            return true;
        } catch (error) {
            return false;
        }
    };
      

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
                            <img src={`${process.env.PUBLIC_URL}/avatars/${selectedAgentGender}/${selectedAgentPic}.svg`} alt="" />
                            {/* <img src={`${process.env.PUBLIC_URL}/avatars/M/1.svg`} alt="" /> */}
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
                            <div>
                                {reportFinal["Tell me about yourself"].split('\n\n').map((paragraph, index) => (
                                    <div key={index}>
                                        {paragraph.split('\n').map((line, lineIndex) => (
                                            <p key={lineIndex}>{line}</p>
                                        ))}
                                    </div>
                                ))}
                            </div>
                        ) : (
                            <p>No report available</p>
                        )}
                    </div>
                    <div className="subheadtwo">
                        <div>
                            <h5>Interests & hobbies</h5>
                            {dictionaryLength > 0 ? (
                                <div>
                                    {reportFinal["Interests & hobbies"].split('\n\n').map((paragraph, index) => (
                                        <div key={index}>
                                            {paragraph.split('\n').map((line, lineIndex) => (
                                                <p key={lineIndex}>{line}</p>
                                            ))}
                                        </div>
                                    ))}
                                </div>
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
                                <div>
                                    {reportFinal["Personality traits"].split('\n\n').map((paragraph, index) => (
                                        <div key={index}>
                                            {paragraph.split('\n').map((line, lineIndex) => (
                                                <p key={lineIndex}>{line}</p>
                                            ))}
                                        </div>
                                    ))}
                                </div>
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
                                <div>
                                    {reportFinal['Thoughts on problem'].split('\n\n').map((paragraph, index) => (
                                        <div key={index}>
                                            {paragraph.split('\n').map((line, lineIndex) => (
                                                <p key={lineIndex}>{line}</p>
                                            ))}
                                        </div>
                                    ))}
                                </div>
                            ) : (
                                <p>No report available</p>
                            )}
                    </div>

                    <div className="subheadfour">
                        <h5>Analysis of your competitors</h5>
                        {/* <p>I am a Gen Z recent college graduate living in New York City. I work in software engineering and earn above $200,000/yr. I’m originally from Chicago and attended Cornell.</p> */}
                        {dictionaryLength > 0 ? (
                                <div>
                                    {reportFinal["Competitors"].split('\n\n').map((paragraph, index) => (
                                        <div key={index}>
                                            {paragraph.split('\n').map((line, lineIndex) => (
                                                <p key={lineIndex}>{line}</p>
                                            ))}
                                        </div>
                                    ))}
                                </div>
                            ) : (
                                <p>No report available</p>
                            )}
                    </div>


                    <div className="subheadfive">
                        <h5>Thoughts on your product</h5>
                        {/* <p>I am a Gen Z recent college graduate living in New York City. I work in software engineering and earn above $200,000/yr. I’m originally from Chicago and attended Cornell.</p> */}
                        {dictionaryLength > 0 ? (
                                <div>
                                    {reportFinal["Thoughts on product"].split('\n\n').map((paragraph, index) => (
                                        <div key={index}>
                                            {paragraph.split('\n').map((line, lineIndex) => (
                                                <p key={lineIndex}>{line}</p>
                                            ))}
                                        </div>
                                    ))}
                                </div>
                            ) : (
                                <p>No report available</p>
                            )}
                    </div>

                    <div className="subheadsix">
                        <div>
                            <h5>Questions & concerns</h5>
                            {dictionaryLength > 0 ? (
                                <div>
                                    {reportFinal["Concerns about product"].split('\n\n').map((paragraph, index) => (
                                        <div key={index}>
                                            {paragraph.split('\n').map((line, lineIndex) => (
                                                <p key={lineIndex}>{line}</p>
                                            ))}
                                        </div>
                                    ))}
                                </div>
                            ) : (
                                <p>No report available</p>
                            )}
                            
                            {/* <ul>
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
                            </ul> */}
                        </div>
                    </div>

                    <div className="sum">
                        <h5>Summary</h5>
                        {dictionaryLength > 0 ? (
                            canParseJSON(reportFinal["Scores"]) ? (
                                <div style={{ display: 'flex', justifyContent: 'center' }}>
                                    {Array.from(JSON.parse(reportFinal["Scores"])).map((score, index) => (
                                        <div key={index} style={{ marginLeft: index === 0 ? '150px' : '0', marginRight: index === 1 ? '130px' : '150px', textAlign: 'center' }}>
                                            <ProgressCircle progress={parseFloat(score).toFixed(2)} />
                                            <p style={{ marginTop: '5px' }}>
                                                {parseFloat(score).toFixed(2)} - {getMetricName(index)}
                                            </p>
                                        </div>
                                    ))}
                                </div>
                            ) : (
                                <p>Scores cannot be displayed. Please check the data format.</p>
                            )
                        ) : (
                            <p>No report available</p>
                        )}
                       
                    </div>

                    <Link to="/interface" className="link-no-underline"> 
                    <div className='reportbutton'>
                        <button
                        disabled={true}
                        >
                        Chat Coming Soon
                        </button>
                    </div>        
                    </Link>
                    
                </div>    
            </div>
        </div>
    </section>
)

}

export default Report