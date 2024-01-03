import React from 'react'
import { Link } from 'react-router-dom';
import { useEffect, useState } from 'react';
import LeftSidebarinterviews from './Leftsidebarinterviews'
import CircularProgress from '@mui/material/CircularProgress';
import { jwtDecode } from "jwt-decode";

function ReportPopup() {
  const [problem, setProblem] = useState('');
  const [product, setProduct] = useState('');
  const [isLoading, setLoading] = useState(true);
  const [buttonClicked, setButtonClicked] = useState(false);
  const selectedAgentName = sessionStorage.getItem('selectedAgentName');
  const token = sessionStorage.getItem('token');
  console.log(token)

  const decoded = jwtDecode(token);
  console.log(decoded);
  // Now you can access the user data in the decoded object

  console.log("HERERERERERERERE")
  const { user: userObject } = decoded;
  console.log(userObject);

  const clearInformation = () => {
    setProblem('');
    setProduct('');
  };

  const handleNewReport = async () => {
    try {
      if (problem.trim() === '' || product.trim() === '') {
        // If any field is empty, prevent the new persona action
        alert('Please fill in all the fields to create a new persona.');
        return;
      }
      console.log("Is it reaching here")
      console.log("User email", userObject.email)
      const email = JSON.stringify({ email: userObject.email })
      console.log("email")
      const interviewResponse = await fetch(`https://alias-testing-130265f16331.herokuapp.com/interview?agent=${selectedAgentName}&email=${'rbp94@cornell.edu'}&problem=${problem}&product=${product}`);
      const responseData = await interviewResponse.json();

      console.log('Response:', responseData);
      const checkkey = product + selectedAgentName
      console.log("Checking for key", checkkey)
      const checkCreate = () => {
        // const checkkey = product + selectedAgentName
        // console.log("Checking for key", checkkey)
        fetch(`https://alias-testing-130265f16331.herokuapp.com/check?key=${checkkey}`)
          .then(response => response.json())
          .then(data => {
            if (data && data.status === 'finished') {
              setLoading(false);
              const reportdata = fetch(`https://alias-testing-130265f16331.herokuapp.com/checkval?key=${checkkey}`)
              console.log("report data complete")
                .then(response => response.json())

              // Add report to PostgreSQL
              fetch('https://alias-node-9851227f2446.herokuapp.com/add-report', {
                method: 'POST',
                headers: {
                  'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                  report: reportdata,
                }),
              })
                .then(response => {
                  if (response.ok) {
                    console.log('New report added successfully to PostgreSQL');
                  } else {
                    console.error('Failed to add new report to PostgreSQL');
                  }
                })
                .catch(error => {
                  console.error('Error while adding new report to PostgreSQL:', error);
                });
            } else {
              // setLoading(true);
              setTimeout(checkCreate, 10000);
            }
          })
          .catch((error) => {
            console.error('Error:', error);
          });
      };

      // Start the recursive call
      checkCreate();
    } catch (error) {
      console.error('Error creating report:', error);
    }


    // Call the fetchInterview function

    //     try {
    //         console.log('Response:', response);
    //         const checkCreate = () => {
    //           fetch(`https://alias-testing-130265f16331.herokuapp.com/check?key=${product}`)
    //             .then(response => response.json())
    //             .then(data => {
    //               if (data && data.status === 'finished') {
    //                 setLoading(false);
    //               } else {
    //                 // setLoading(true);
    //                 setTimeout(checkCreate, 10000);
    //               }
    //             })
    //             .catch((error) => {
    //               console.error('Error:', error);
    //             });
    //         };

    //         // Start the recursive call
    //         checkCreate();

    //         fetch('https://alias-node-9851227f2446.herokuapp.com/add-report', {
    //             method: 'POST',
    //             headers: {
    //             'Content-Type': 'application/json',
    //             },
    //             body: JSON.stringify({
    //                 report: response
    //             }),
    //         })
    //             .then(response => {
    //             if (response.ok) {
    //                 console.log('New report added successfully to postgres');
    //                 // Ensure loading indicator is turned off after completion
    //             } else {
    //                 console.error('Failed to add new report to postfres');
    //             }
    //             })
    //             .catch(error => {
    //             console.error('Error while adding new report to postgres:', error);
    //             }); 

    //       }
    //       catch (error) {
    //         console.error('Error creating report:', error);
    //       } 
    //     } 
    //   catch (error) {
    //     console.error('Error:', error);
    //   }
  }

  const handleNewReportClick = async () => {
    try {
      await handleNewReport(); // Call the new persona function
    } catch (error) {
      console.error('Error:', error);
    }
  };

  useEffect(() => {
    if (!isLoading && buttonClicked) {
      // Redirect to the "/person" page
      // You may use react-router-dom's history or any other method for redirection
      window.location.href = "/reports";
    }
  }, [isLoading, buttonClicked]);

  return (


    <section className='home container-fluid'>
      <div className="row">
        <div className="col-md-4">
          <LeftSidebarinterviews />
        </div>
      </div>

      <div className="col-md-8 big">
        <div className="big-inner-childs-popup">
          <Link to="/interviews">
            <button className="backarrow"> <img src="./Arrow-Left.svg" /> </button>
          </Link>
          <div className="personcardpopup">
            <h4>Create your interview</h4>
            <div className="mtextarea pt-5">
              <label htmlFor="Problem">What problem are you trying to solve?</label><br></br>
              <textarea
                cols="80"
                rows="5"
                placeholder="e.g The student loan crisis. Gen Z recent college graduates lack financial literacy to manage finances and repay debt"
                value={problem}
                onChange={(e) => setProblem(e.target.value)}
              ></textarea>
            </div>

            <div className="mtextarea pt-5">
              <label htmlFor="Product">What is your solution or product?</label><br></br>
              <textarea
                cols="80"
                rows="5"
                placeholder="e.g An app that tracks personal finances of recent graduates"
                value={product}
                onChange={(e) => setProduct(e.target.value)}
              ></textarea>
            </div>

            <div className="mbuttonarea text-center">

              <Link
                to={
                  !isLoading && problem.trim() !== '' && product.trim() !== ''
                    ? "/reports"
                    : "#"
                }
              >
                <button
                  className='customButton'
                  onClick={() => {
                    setButtonClicked(true);
                    setLoading(true);
                    handleNewReportClick();
                  }}
                >
                  {
                    isLoading && buttonClicked ? (
                      <CircularProgress size={24} color="inherit" />
                    ) : (
                      'New Interview'
                    )
                  }
                </button>
              </Link>

              <button class='customButton transp' onClick={clearInformation}>Clear Information</button>
            </div>
          </div>
        </div>
      </div>
    </section>

  )
}

export default ReportPopup