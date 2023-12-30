import React from 'react'
import { Link } from 'react-router-dom';
import LeftSidebarinterviews from './Leftsidebarinterviews'

function Report() {
    const selectedAgentName = sessionStorage.getItem('selectedAgentName');
    const selectedAgentPic = sessionStorage.getItem('selectedAgentPic');
    const selectedAgentGender = sessionStorage.getItem('selectedAgentGender');
    const selectedAgentAge = sessionStorage.getItem('selectedAgentAge');
    const selectedAgentJob = sessionStorage.getItem('selectedAgentJob');


return (
    <section className='home container-fluid'>
        <div className="row">
        <div className="col-md-4">
          <LeftSidebarinterviews/>
        </div>  
        </div>
        <div className="col-md-8 big">
            <div className="big-inner-child">
                <div className="big-inner-reports">
                    <div className="int">
                        <div className="intimg">
                            {/* <img src={`${process.env.PUBLIC_URL}/avatars/${selectedAgentGender}/${selectedAgentPic}.svg`} alt="" /> */}
                            <img src={`${process.env.PUBLIC_URL}/avatars/M/1.svg`} alt="" />
                        </div>
                        <div className="inttext">
                            {/* <h4>{selectedAgentName}</h4> */}
                            <h4>Chris Lopez</h4>
                            {/* <p>{selectedAgentAge} yrs - {selectedAgentJob}</p> */}
                            <p>20 yrs - Software Engineer</p>
                        </div>
                    </div>
                    <div className="subhead">
                        <h5>About me</h5>
                        <p>I am a Gen Z recent college graduate living in New York City. I work in software engineering and earn above $200,000/yr. I’m originally from Chicago and attended Cornell.</p>
                    </div>
                    <div className="subheadtwo">
                        <div>
                            <h5>Interests & hobbies</h5>
                            <ul>
                                <li>Playing video games since a child</li>
                                <li>Stock trading with college friends</li>
                                <li>Testing new products after buying first iPhone</li>
                            </ul>
                        </div>
                        
                        <div>
                            <h5>Personality traits</h5>
                            <ul>
                                <li>Introverted</li>
                                <li>Apprehensive to new experiences</li>
                                <li>Compassionate</li>
                            </ul>
                        </div>

                    </div>
                    <div className="subheadthree">
                        <h5>Pain points</h5>
                        <p>I am a Gen Z recent college graduate living in New York City. I work in software engineering and earn above $200,000/yr. I’m originally from Chicago and attended Cornell.</p>
                    </div>

                    <div className="subheadfour">
                        <h5>Analysis of your competitors</h5>
                        <p>I am a Gen Z recent college graduate living in New York City. I work in software engineering and earn above $200,000/yr. I’m originally from Chicago and attended Cornell.</p>
                    </div>


                    <div className="subheadfive">
                        <h5>Thoughts on your product</h5>
                        <p>I am a Gen Z recent college graduate living in New York City. I work in software engineering and earn above $200,000/yr. I’m originally from Chicago and attended Cornell.</p>
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
                       
                    </div>
{/* 
                    <Link to="/interface" onClick={() => handleInterviewClick(name)}> */}
                    <div className='reportbutton'>
                            <button>Open Chat</button>
                    </div>        
                        {/* </Link> */}
                    
                </div>    
            </div>
        </div>
    </section>
)

}

export default Report