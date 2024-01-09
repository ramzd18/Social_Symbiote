import Leftsidebar from './Leftsidebar'
import React, { useState, useEffect } from 'react';
// import { Marketstat } from './Marketstat';
import ProgressCircle from './ProgressCircle';
import { Marketstat } from './Marketstat';
import { inputAdornmentClasses } from '@mui/material';
import { jwtDecode } from "jwt-decode";
import LeftSidebarmarketing from './LeftSidebarmarketing';

function Usabillity() {
  console.log("testing logging")
  const [agentNames, setAgentNames] = useState([]);
  const [agentName, setAgentName] = useState('');
  const [buttonInfo, setButtonInfo] = useState(null);
  const [inputValue, setInputValue] = useState('');
  const [contextValue, setContextValue] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [show, setShow] = useState(false);
  const [selectedValue, setSelectedValue] = useState('');
  const [formattedList, setFormattedList] = useState([]);
  const token = sessionStorage.getItem('token');
  console.log(token)

  const decoded = jwtDecode(token);
  const { user: userObject } = decoded;



  const handleclick = async () => {
    setIsLoading(true);
    console.log(inputValue);
    console.log(contextValue);
    // console.log(selectedValue);
    const emailval = userObject.email
    const data = await fetch(`https://alias-testing-130265f16331.herokuapp.com/usecheck?url=${inputValue}&context=${contextValue}&name=${selectedValue.toLowerCase()}&email=${emailval}`)
    console.log("AFTER LIGGING")
    // const data = await fetch('http://127.0.0.1:5000/usecheck?name=nick&email=rbp94@cornell.edu&url=https://www.reddit.com/&context=A%20social%20media%20site%20that%20allows%20users%20to%20post%20anything%20they%20want')

    const checkCreate = () => {
      // const checkkey = product + selectedAgentName
      const checkkey = selectedValue + contextValue
      fetch(`https://alias-testing-130265f16331.herokuapp.com/check?key=${checkkey}`)
        .then(response => response.json())
        .then(data => {
          if (data && data.status === 'finished') {
            //   const reportdata = fetch(`https://alias-testing-130265f16331.herokuapp.com/checkval?key=${checkkey}`)
            //   console.log("report data complete")
            const arrayval = data.data;
            const arrayval1 = JSON.parse(arrayval)
            console.log("array data", arrayval)
            console.log("FIRST VALUE", arrayval[0])
            console.log("LAST RESPONSE", arrayval[4])
            setButtonInfo(<Marketstat clarity={arrayval1[0]} personalization={arrayval1[1]} impact={arrayval1[2]} retention={arrayval1[3]} message={arrayval1[4]} />);
            setIsLoading(false);



          } else {
            // setLoading(true);
            setTimeout(checkCreate, 10000);
          }
        })
        .catch((error) => {
          console.error('Error:', error);
        });
    };


    checkCreate();
    // fetch(`http://127.0.0.1:5000/marketing?tagline=${inputValue}&context=${contextValue}&name=${selectedValue.toLowerCase()}`)
    //   .then(response => response.json())
    //   .then(data => {
    //     const array = data;
    //     setButtonInfo(<Marketstat clarity={array[0]} personalization={array[1]} impact={array[2]} retention={array[3]} message={array[4]} />);
    //     setIsLoading(false);
    //   })
    //   .catch(error => {
    //     console.error('Error:', error);
    //     setIsLoading(false);
    //   });
    // setIsLoasing(false)

    // setButtonInfo(<Marketstat clarity={.2} personalization={.8} impact={.4} retention={.6} message='This is the optimized tailored marketing message' />

    setShow(true);
  };
  async function fetchData() {
    try {
      const response = await fetch(`https://alias-node-9851227f2446.herokuapp.com/getAgentName`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email: userObject.email }),
      });
      const data = await response.json();
      console.log('Response:', data); // Log the full response

      if (data.names) {
        console.log('Multiple Names:', data.names);
        return data.names; // This will be an array
      } else if (data.name) {
        console.log('Single Name:', data.name);
        return [data.name]; // This will also be an array
      } else {
        return []; // Ensures that the return value is always an array
      }
    } catch (error) {
      console.error('Error:', error);
      return []; // Return an empty array in case of error
    }
  }
  // try {
  //   const response = await fetch('http://127.0.0.1:5000/agentslist');
  //   const data = await response.json();
  //   if (Array.isArray(data.data)) {
  //     return data.data.map((value, index) => ({
  //       value: value.charAt(0).toUpperCase() + value.slice(1),
  //       label: `Option ${index + 1}`
  //     }));
  //   } else {
  //     console.error('Data received is not an array:', data.data);
  //     return [];
  //   }
  // } catch (error) {
  //   console.error('Error fetching data:', error);
  //   return [];
  // }



  useEffect(() => {
    fetchData().then(data => {
      setFormattedList(data); // data will always be an array because fetchData ensures it
    });
  }, []);

  // { value: 'Jake', label: 'Option 1' },
  // { value: 'john', label: 'Option 2' },
  // { value: 'Brenda', label: 'Option 3' }
  // Add more options as needed

  return (
    <section className='home container-fluid'>
      {/*<div className="logo-section "> </div> */}

      <div className="row">
        <div className="col-md-4">
          <LeftSidebarmarketing />
        </div>
        { }
      </div>
      <div className="col-md-8 big">
        <div className="big-inner-child">
          <h2 className='pb-5'>Usabillity Testing</h2>
          <div className="mark-big-inner-interviews">
            <div className="int">
              <h4>Test your software with our agents</h4>
              <div style={{ padding: '10px', }}>
                <input style={{ width: '300px', margn: '10px' }}
                  type="text"
                  value={inputValue}
                  placeholder="Enter your url i.e localhost:300"
                  onChange={(e) => setInputValue(e.target.value)}
                />
                <input style={{ width: '400px', margin: '10px' }}
                  type="text"
                  value={contextValue}
                  placeholder="Enter context for your website, i.e a social media platform that connects travelers"
                  onChange={(e) => setContextValue(e.target.value)}
                />
                <select
                  value={selectedValue}
                  onChange={(e) => setSelectedValue(e.target.value)}
                  style={{ width: '15%', height: '20%', margin: '15x' }}
                >
                  <option value="">Select Person</option>
                  {formattedList && formattedList.map((name, index) => (
                    <option key={index} value={name}>
                      {name}
                    </option>
                  ))}
                </select>

                <button onClick={() => handleclick()} style={{ padding: '5px', margin: '15px' }}>
                  Submit
                </button>
              </div>
              {isLoading &&
                <p>Loading...</p>
              }
            </div>
            {show && buttonInfo}
          </div>
        </div>
      </div>
    </section>

  )

}
export default Usabillity