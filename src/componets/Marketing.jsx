import Leftsidebar from './Leftsidebar'
import LeftSidebarmarketing from './LeftSidebarmarketing';
import LeftSidebarinterviews from './Leftsidebarinterviews'
import React, { useState, useEffect } from 'react';
// import { Marketstat } from './Marketstat';
import ProgressCircle from './ProgressCircle';
import { Marketstat } from './Marketstat';
import { inputAdornmentClasses } from '@mui/material';




// .then(resp => resp.json())
// .then(data => {
//   data.data;
// });

function Marketing() {
  console.log("testing logging")
  const [buttonInfo, setButtonInfo] = useState(null);
  const [inputValue, setInputValue] = useState('');
  const [contextValue, setContextValue] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [show, setShow] = useState(false);
  const [selectedValue, setSelectedValue] = useState('');
  const [formattedList, setFormattedList] = useState([]);

  const handleclick = () => {
    setIsLoading(true);
    console.log(inputValue);
    console.log(contextValue);
    console.log(selectedValue);
    fetch(`http://127.0.0.1:5000/marketing?tagline=${inputValue}&context=${contextValue}&name=${selectedValue.toLowerCase()}`)
      .then(response => response.json())
      .then(data => {
        const array = data;
        setButtonInfo(<Marketstat clarity={array[0]} personalization={array[1]} impact={array[2]} retention={array[3]} message={array[4]} />);
        setIsLoading(false);
      })
      .catch(error => {
        console.error('Error:', error);
        setIsLoading(false);
      });
    // setIsLoasing(false)

    // setButtonInfo(<Marketstat clarity={.2} personalization={.8} impact={.4} retention={.6} message='This is the optimized tailored marketing message' />

    setShow(true);
  };
  async function fetchData() {
    try {
      const response = await fetch('http://127.0.0.1:5000/agentslist');
      const data = await response.json();
      if (Array.isArray(data.data)) {
        return data.data.map((value, index) => ({
          value: value.charAt(0).toUpperCase() + value.slice(1),
          label: `Option ${index + 1}`
        }));
      } else {
        console.error('Data received is not an array:', data.data);
        return [];
      }
    } catch (error) {
      console.error('Error fetching data:', error);
      return [];
    }
  }


  useEffect(() => {
    // Replace fetchData() with the actual function to fetch data
    fetchData().then(data => {
      setFormattedList(data);
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
          <h2 className='pb-5'>Marketing Analysis</h2>
          <div className="mark-big-inner-interviews">
            <div className="int">
              <h4>Enter your tagline</h4>
              <div style={{ padding: '10px', }}>
                <input style={{ width: '300px', margn: '10px' }}
                  type="text"
                  value={inputValue}
                  placeholder="Enter your tagline"
                  onChange={(e) => setInputValue(e.target.value)}
                />
                <input style={{ width: '400px', margin: '10px' }}
                  type="text"
                  value={contextValue}
                  placeholder="Enter context for you company, i.e: A healthy alternative energy drink brand"
                  onChange={(e) => setContextValue(e.target.value)}
                />
                <select value={selectedValue} onChange={(e) => setSelectedValue(e.target.value)} style={{ width: '15%', height: '20%', margin: '15x' }}>
                  <option value="">Select Person</option>
                  {formattedList.map((item, index) => (
                    <option key={index} value={item.value}>
                      {item.value}
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
export default Marketing