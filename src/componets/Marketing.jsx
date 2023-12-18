import Leftsidebar from './Leftsidebar'
import LeftSidebarinterviews from './Leftsidebarinterviews'
import React, { useState } from 'react';
// import { Marketstat } from './Marketstat';
import ProgressCircle from './ProgressCircle';
import { Marketstat } from './Marketstat';

function Marketing() {
  const [buttonInfo, setButtonInfo] = useState(null);
  const [inputValue, setInputValue] = useState('');
  const [isLoading, setIsLoasing] = useState(false)
  const [show, setShow] = useState(false);
  const [selectedValue, setSelectedValue] = useState('');

  const handleclick = (message) => {
    setButtonInfo(<Marketstat clarity={.2} personalization={.8} impact={.4} retention={.6} message='This is the optimized tailored marketing message' />
    );
    setShow(true);
  };
  const options = [
    { value: 'Jake', label: 'Option 1' },
    { value: 'john', label: 'Option 2' },
    { value: 'Brenda', label: 'Option 3' }
    // Add more options as needed
  ];
  return (
    <section className='home container-fluid'>
      {/*<div className="logo-section "> </div> */}

      <div className="row">
        <div className="col-md-4">
          <LeftSidebarinterviews />
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
                <input style={{ width: '40%', }}
                  type="text"
                  value={inputValue}
                  onChange={(e) => setInputValue(e.target.value)}
                />
                <select value={selectedValue} onChange={(e) => setSelectedValue(e.target.value)} style={{ width: '15%', height: '20%', margin: '15x' }}>
                  <option value="">Select Person</option>
                  {options.map(option => (
                    <option key={option.value} value={option.value}>
                      {option.label}
                    </option>
                  ))}
                </select>
                <button onClick={() => handleclick(inputValue)} style={{ padding: '5px', margin: '15px' }}>
                  Submit
                </button>
              </div>
            </div>
            {show && buttonInfo}
          </div>
        </div>
      </div>
    </section>

  )

}
export default Marketing