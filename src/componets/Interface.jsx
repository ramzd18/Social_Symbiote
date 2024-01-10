import React from 'react'
import LeftSidebarinterviews from './Leftsidebarinterviews'
import {useState , useEffect, useRef } from 'react';

import Message from './message'
import { Link } from 'react-router-dom';
import { jwtDecode } from "jwt-decode";
import CircularProgress from '@mui/material/CircularProgress';


function Interface() {
  //const { currentChat, saveMessages } = useContext(ChatContext)
  const [isLoading, setIsLoading] = useState(false)
  const [rows, setRows] = useState(1);
  const textAreaRef = useRef(null);
  const [message, setMessage] = useState('');
  const [conversation, setConversation] = useState([])
  const [agentPics, setAgentPics] = useState([]);
  const [agentPic, setAgentPic] = useState('');
  const [isInterviewActive, setIsInterviewActive] = useState(true);
  const selectedAgentName = sessionStorage.getItem('selectedAgentName');
  const selectedAgentGender = sessionStorage.getItem('selectedAgentGender');
  const selectedAgentPic = sessionStorage.getItem('selectedAgentPic');
  const token = sessionStorage.getItem('token');
  const decoded = jwtDecode(token);
  const { user: userObject } = decoded;
  const email = userObject.email;

  // const apiBaseUrl = process.env.NODE_ENV === 'production'
  // ? 'https://alias-testing.herokuapp.com'
  // : 'http://localhost:5433';

  console.log(selectedAgentName);
  console.log(email);


  const handleInput = (e) => {
    const text = e.target.value;
    setMessage(text);
    const lineHeight = 70; // Adjust according to your text area's line height
    const maxRows = 3; // Maximum rows allowed
  
    const lines = (textAreaRef.current.value + '\n').match(/\n/g).length || 1; // Count the number of lines
  
    // Calculate the current height of the text area
    const currentHeight = textAreaRef.current.scrollHeight;
  
    // Calculate the maximum height when the row limit is reached
    const maxHeight = lineHeight * maxRows;
  
    // If the current height is greater than the maximum height, don't add a new line
    if (currentHeight >= maxHeight) {
      textAreaRef.current.value = textAreaRef.current.value.slice(0, -1);
      return;
    }
  
    // Calculate the number of rows based on the current height
    const calculatedRows = Math.ceil(currentHeight / lineHeight);
  
    // Set the rows based on the calculated rows, capped at the maximum rows
    textAreaRef.current.rows = Math.min(calculatedRows, maxRows);
  }  

  const sendMessage = async () => {
    console.log('Sending message:', message);


    const sentMessage = {
      content: message,
      role: 'user',
    };

    

    setConversation(prevConversation => [...prevConversation, sentMessage]);
    setMessage('');

    setIsLoading(true);


  try {
    const response = await fetch(`https://alias-testing-130265f16331.herokuapp.com/load_response?name=${selectedAgentName}&email=${email}&question=${message}`);
    const data = await response.text();
    
    console.log('Response from server:', data);

    const receivedMessage = {
      content: data,
      role: 'assistant',
    };

    setConversation(prevConversation => [...prevConversation, receivedMessage]);
  } catch (error) {
    console.error('Error processing response:', error);
  } finally {
    setIsLoading(false); // Set loading state to false after receiving a response
  }
};



    //setIsLoading(true);
    // setConversation?.([...conversation!, { content: input, role: 'user' }])

    {/*try {
      const response = await postChatOrQuestion(currentChat, conversation, input);

      if (response.ok) {
        const data = response.body;

        if (!data) {
          throw new Error('No data');
        }

        const reader = data.getReader();
        const decoder = new TextDecoder('utf-8');
        let done = false;
        let resultContent = '';

        while (!done) {
          const { value, done: readerDone } = await reader.read();
          const char = decoder.decode(value);
          if (char) {
            resultContent += char;
          }
          done = readerDone;
        }

        setTimeout(() => {
          setConversation([
            ...(conversation ?? []),
            { content: input, role: 'user' },
            { content: resultContent, role: 'assistant' },
          ]);
          setCurrentMessage('');
        }, 1);
      } else {
        const result = await response.json();
        toast.error(result.error);
      }

      setIsLoading(false);
    } catch (error) {
      console.error(error);
      toast.error(error.message);
      setIsLoading(false);
    }

  */}



  const handleKeyPress = (event) => {
    if (event.key === 'Enter' && event.target.id === 'interviewInput' && !event.shiftKey) {
      event.preventDefault();
      sendMessage();
    }
  };

  /*const clearAgentName = () => {
    sessionStorage.removeItem('selectedAgentName');
    console.log(sessionStorage.getItem('selectedAgentName'));
  }; */


  const handleBack = () => {

    fetch(`https://alias-node-9851227f2446.herokuapp.com/updateChatHistory`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ name: selectedAgentName, personEmail: email, conversation: conversation }),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log('Response from server:', data); // Check the response data
        // Further processing based on the response data
        try {
          const chatHistory = JSON.parse(data.chatHistory);
    
          // Check the parsed chatHistory object
          console.log('Parsed chatHistory:', chatHistory);
          
    
          // Further processing based on the chat history
          // ...
        } catch (error) {
          console.error('Invalid JSON format for chat history:', error);
        }
      })
      .catch((error) => {
        console.error('Error:', error); // Log any fetch errors
      });

    sessionStorage.removeItem('selectedAgentName');
  }


  useEffect(() => {

  
    const interviewInput = document.getElementById('interviewInput');

  if (interviewInput) {
    console.log('Adding event listener to interviewInput');
    interviewInput.addEventListener('keypress', handleKeyPress);
  }

  return () => {
    if (interviewInput) {
      console.log('Removing event listener from interviewInput');
      interviewInput.removeEventListener('keypress', handleKeyPress);
    }
  };
  }, [sendMessage]);


  // useEffect(() => {
  //   fetch('http://localhost:5433/getAgentPic', {
  //           method: 'POST',
  //           headers: {
  //           'Content-Type': 'application/json',
  //           },
  //           body: JSON.stringify({ email: userObject.email }), // Ensure the body is an object
  //       })
  //       .then((response) => response.json()) // Try parsing response as JSON
  //       .then((data) => {
  //           {/* console.log('Response:', data.name); // Log the full response
  //           setAgentName(data.name);
  //           */}
  //           if (data.pics) {
  //               console.log('Multiple pics:', data.pics);
  //               // Store the array in the state or variable
  //               setAgentPics(data.pics);
  //               setAgentPic('');
  //           } else if (data.pic) {
  //               console.log('Single pic:', data.pic);
  //               // Handle a single name separately
  //               setAgentPic(data.pic);
  //               setAgentPics([]);
  //           } else {
  //               console.error('Error:', data); // Log any unexpected response
  //           }
  //           // ... rest of your code
  //       })
  //       .catch((error) => console.error('Error:', error));
  // }, []);

  useEffect(() => {
    // Fetch the conversation messages on component load
    if (isInterviewActive) {
      fetch(`https://alias-node-9851227f2446.herokuapp.com/getConversation`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ name: selectedAgentName, personEmail: email }),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log('Response from server:', data); // Check the response data
        if (Array.isArray(data.messages) && data.messages.length > 0) {
          const formattedMessages = data.messages.map((msg) => ({
            content: msg.content,
            role: msg.role,
          }));
          setConversation(formattedMessages);
          setIsInterviewActive(false);
        }
      })
      .catch((error) => {
        console.error('Error fetching conversation:', error);
      });
    }
}, [isInterviewActive]);
  

  return (
    <>
     <section className='home container-fluid'>
   {/* <div className="logo-section ">
    
  </div> */}
    <div className="row">
        <div className="col-md-4">
          <LeftSidebarinterviews/>
        </div>  
    {/*<div className="left-sidebar">
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
        {/*<div class="border-line"></div> */}
       <div className="col-md-8 big-interface">
            <Link to="/reports" onClick={handleBack}>
              <button className="backarrowinterface"> <img src= "./Arrow-Left.svg" /> </button>
      
            </Link>
         
         {/* <div className="big-inners"> */}

          {/*} chat history from git, render right box from git, send message from chat from git, load agent info including image from data recorded in interviews.jsx", connect agent to respond from git> */}

          <div className="chat-container">
            {conversation.map((message, index) => (
              <div key={index} className={message.role === 'user' ? 'sent-message' : 'received-message'}>
                <img src={message.role === 'user' ? './Users Icons.svg' : `${process.env.PUBLIC_URL}/avatars/${selectedAgentGender}/${selectedAgentPic}.svg`} alt="" />
                <p>{message.content}</p>
              </div>
            ))}
          </div>

          {/* <div className="sent-messages-container">
            {console.log('Sent messages:', conversation)}
            {conversation.length > 0 && conversation.map((message, index) => (
                message.role === 'user' && (
                    <div className="sent-message" key={index}>
                        <img src="./Users Icons.svg" alt="" />
                        <p>{message.content}</p>
                    </div>
                )
            ))}
        </div>

        <div className="received-messages-container">
          {console.log('received messages:', conversation)}
          {conversation.length > 0 && conversation.map((message, index) => (
            message.role === 'assistant' && (
              <div className="received-message" key={index}>
                <img src={`${process.env.PUBLIC_URL}/avatars/${selectedAgentGender}/${selectedAgentPic}.svg`} alt="" />
                <p>{message.content}</p>
              </div>
            )
          ))}
        </div> */}

          {/*}  
           <div className="interviewtext">
            <div className="innerinterviewtext">
                <div className="interimg">
                    <img src="./Ellipse 63 (1).png" alt="" />
                </div>
                <div className="intertexts">
                    <h5>Interesting. Do you have an idea for a solution?
</h5>

                </div>
            </div>
            <div className="interviewbuttons">
                <button>The problem we want to solve is the student debt crisis.</button>
            </div>
           </div>

      */}
         
           
          
          {/*</div> */}
          {/* <div className="big-interface-inner-child"> */}
         {/* <div className="intervieinputs"> */}
          {/*}
            <div className="tags">
                <span>Concept Testing</span>
                <span>Problem Exploration</span>
                <span>Design Feedback</span>
                <span>Campaign Testing</span>
                <span>Ad Testing</span>
            </div>
      */}
        <div className="input-container">
            <textarea
              placeholder="Ask a question."
              id="interviewInput" 
              className="input-box"
              ref={textAreaRef}
              rows={rows}
              value={message}
              onInput={handleInput}
              onKeyDown={handleKeyPress}
            />
            <button onClick={sendMessage}>
            {isLoading ? (
              <CircularProgress size={24} color="inherit" />
            ) : (
              <img src="./Reply.svg" alt="Reply" />
            )}
          </button>
            
         </div>
        </div> 
         {/* </div> */}
           
        {/* </div> */}
    </section></>
  )
}

export default Interface