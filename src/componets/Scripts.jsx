import React from 'react'
import LeftSidebarinterviews from './Leftsidebarinterviews'
import { useState, useEffect, useRef } from 'react';

import Message from './message'
import { Link } from 'react-router-dom';
import { jwtDecode } from "jwt-decode";
import CircularProgress from '@mui/material/CircularProgress';
import LeftSidebarmarketing from './LeftSidebarmarketing';
import QuestionsList from './Questionslist';

function Scripts() {
  //const { currentChat, saveMessages } = useContext(ChatContext)
  // const [isLoading, setIsLoading] = useState(false)
  // const [rows, setRows] = useState(1);
  // const textAreaRef = useRef(null);
  // const [message, setMessage] = useState('');
  // const [conversation, setConversation] = useState([])
  // const [agentPics, setAgentPics] = useState([]);
  // const [agentPic, setAgentPic] = useState('');
  // const [isInterviewActive, setIsInterviewActive] = useState(true);
  // const selectedAgentName = sessionStorage.getItem('selectedAgentName');
  // const selectedAgentGender = sessionStorage.getItem('selectedAgentGender');
  // const selectedAgentPic = sessionStorage.getItem('selectedAgentPic');
  // const token = sessionStorage.getItem('token');
  // const decoded = jwtDecode(token);
  // const { user: userObject } = decoded;
  // const email = userObject.email;

  // const apiBaseUrl = process.env.NODE_ENV === 'production'
  // ? 'https://alias-testing.herokuapp.com'
  // : 'http://localhost:5433';

  // console.log(selectedAgentName);
  // console.log(email);



  return (
    <section className='home container-fluid'>
      {/*<div className="logo-section "> </div> */}

      <div className="row">
        <div className="col-md-4">
          <LeftSidebarmarketing />
        </div>
      </div>
      <div className="col-md-8 big">
        <div className="big-inner-child">

          <QuestionsList />
        </div>
      </div>
    </section>

  )
}

export default Scripts