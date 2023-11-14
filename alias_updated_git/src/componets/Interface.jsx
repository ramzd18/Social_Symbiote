import React from 'react'
import LeftSidebarinterviews from './Leftsidebarinterviews'
import {useState , useEffect, useRef } from 'react';

import Message from './message'
import { Link } from 'react-router-dom';
import { jwtDecode } from "jwt-decode";


function Interface() {
  //const { currentChat, saveMessages } = useContext(ChatContext)
  const [isLoading, setIsLoading] = useState(false)
  const [rows, setRows] = useState(1);
  const textAreaRef = useRef(null);
  const [message, setMessage] = useState('');
  const [conversation, setConversation] = useState([])
  const [agentPics, setAgentPics] = useState([]);
  const [agentPic, setAgentPic] = useState('');
  const selectedAgentName = sessionStorage.getItem('selectedAgentName');
  const selectedAgentGender = sessionStorage.getItem('selectedAgentGender');
  const selectedAgentPic = sessionStorage.getItem('selectedAgentPic');
  const token = sessionStorage.getItem('token');
  const decoded = jwtDecode(token);
  const { user: userObject } = decoded;
  const email = userObject.email;

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

    

    setConversation([...(conversation), sentMessage]);

    fetch(`http://127.0.0.1:5000/load_response?name=${selectedAgentName}&email=${email}&question=${message}`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
    })  
      .then((response) => response.json())
      .then((data) => {
        console.log('Response from server:', data); // Check the response data
  
        try {
          const receivedMessage = {
            content: message,
            role: 'assistant',
          };
      
          setConversation([...(conversation), receivedMessage]);
        } catch (error) {
          console.error('Invalid JSON format for chat history:', error);
        }
      });

    // console.log(conversation);


    setMessage('');



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

  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault(); // Prevents a new line in the textarea

      // Call sendMessage function
      sendMessage();
    }
  };

  /*const clearAgentName = () => {
    sessionStorage.removeItem('selectedAgentName');
    console.log(sessionStorage.getItem('selectedAgentName'));
  }; */


  const handleBack = () => {

    fetch('http://localhost:5433/updateChatHistory', {
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
    const handleKeyUp = (event) => {
      if (event.keyCode === 13 && event.target.id === 'interviewInput' && !event.shiftKey) {
        sendMessage();
      }
    };

    document.addEventListener('keyup', handleKeyUp);

    return () => {
      document.removeEventListener('keyup', handleKeyUp);
    };
  }, []);

  useEffect(() => {
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
  }, []);

  useEffect(() => {
    // Fetch the conversation messages on component load
    fetch('http://localhost:5433/getConversation', {
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
        console.log('Formatted Messages:', formattedMessages);
        setConversation(formattedMessages);
        console.log('New conversation state:', formattedMessages);
      }
    })
    .catch((error) => {
      console.error('Error fetching conversation:', error);
    });
}, []);
  

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
       <div className="col-md-8 big">
            <Link to="/interviews" onClick={handleBack}>
              <button className="backarrowinterface"> <img src= "./Arrow-Left.svg" /> </button>
      
            </Link>
         
         {/* <div className="big-inners"> */}

          {/*} chat history from git, render right box from git, send message from chat from git, load agent info including image from data recorded in interviews.jsx", connect agent to respond from git> */}

          <div className="sent-messages-container">
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
        </div>

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
          <div className="big-inner-child">
         <div className="intervieinputs">
          {/*}
            <div className="tags">
                <span>Concept Testing</span>
                <span>Problem Exploration</span>
                <span>Design Feedback</span>
                <span>Campaign Testing</span>
                <span>Ad Testing</span>
            </div>
      */}
            <textarea
              placeholder="Ask a question."
              id="interviewInput" 
              class="input-box"
              ref={textAreaRef}
              rows={rows}
              value={message}
              onInput={handleInput}
              onKeyDown={handleKeyPress}
            />
            <button onClick={sendMessage}><img src="./Reply.svg" alt="" className='intervieinputimgs'/></button>
            
         </div>
         </div>
           
        </div>
    </section></>
  )
}

export default Interface