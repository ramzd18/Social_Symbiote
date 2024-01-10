import React from 'react'
import { Link } from 'react-router-dom';
import LeftSidebar from './Leftsidebar'

function Home() {
  return (
    <>
    <section className='home container-fluid'>
   {/*<div className="logo-section ">
    
    </div>
    */}

    <div className="row">
        <div className="col-md-4">
          <LeftSidebar/>
        </div>  
        {/*}
        <div className="left-sidebar">
        <div className="sidebartop">
        <div className="logo">
        
        <img src="./aliaslogodarksvg.svg" alt="" srcset="" />
        </div>
        */}

        {/*
        <div className="active">
              <li className=''> <img src="./homewhite.svg" alt="" />Home</li>
        </div>

              <Link to="/person"> 
                <button><img src="./personablack.svg"/> <span> Your personas</span></button> 
              </Link>
              <Link to="/interviews">
                <button><img src="./chatblack.svg"/> <span> User interviews</span></button>
              </Link>  
              </div>
              */}
        {/*
        <div className="sidebarbottom">
        <li> <img src="./tool-02.png" alt="" /> Integrations</li>
        <li> <img src="./users-plus.png" alt="" />Billing</li>
        <li><img src="./help outline.png" alt="" />Support</li>
        </div>
        */}
    </div>
        {/*</div>*/}
        <div className="col-md-8 big">
         <div className="big-inner-child">
         <div className="big-inner">
            <h3>Getting Started</h3>

            <iframe
              src="https://www.loom.com/embed/8b7c53b9d00040ec99ea4da7573d7de9?sid=53c845b5-cb3a-464c-9381-524d5ad097dc"
              allowFullScreen
              style={{ width: '521px', height: '246px' }}
            ></iframe>

            <div className="big-box-button text-center">
                <Link to="/person"> 
                  <button>Create a Persona</button>
                </Link>
                <Link to="/interviews">   
                  <button>Start an Interview</button>
                </Link>
            </div>
           
          </div>
           {/*
           <div className="project">
                <button>Your Projects</button>
                <button>+  New Project</button>
            </div>
          */}  
          </div>
           
        </div>
    </section>
    </>
  )
}

export default Home