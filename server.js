const express = require('express');
const https = require('https');
const mysql = require('mysql');
const bodyParser = require('body-parser');
const path = require('path');
const Knex = require('knex');
const fs = require('fs');
const cors = require('cors');
const { Pool } = require('pg');
const jwt = require('jsonwebtoken');


const app = express();
const port =  process.env.PORT || 5433;
app.set('port', port);

const corsOptions = {
    origin: ['https://www.use-alias.com', 'https://alias-node-9851227f2446.herokuapp.com/'],
    // Add other CORS options as needed
  };
  
app.use(cors(corsOptions));
app.use(bodyParser.json());


const pool = new Pool ({
    // Note: Saving credentials in environment variables is convenient, but not
    // secure - consider a more secure solution such as
    // Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
    // keep secrets safe.

        host: '35.233.155.93',
        user: 'postgres',
        password: 'Jeff@2234',
        database: 'user-agents',
        port: 5432


});



{/*mysql.createConnection({
    host: '35.233.155.93',
    user: 'postgres',
    password: 'Jeff@2234',
    database: 'user-agents',
    connectTimeout: 20000, // Adjust timeout (in milliseconds) as needed
    */}

{/*}
  db.connect((err) => {
    if (err) {
      console.error('Error connecting to the database:', err);
      return;
    }
    console.log('Database connected successfully');
    // Close the database connection after testing
    db.end();
  });  

*/}

app.get('/', (req, res) => {
    res.send('Health check OK');
  });
  

app.post('/createUser', async (req, res) => {
    const { given_name, family_name, email } = req.body;
    console.log('Incoming data:', given_name, family_name, email);
  
    try {
        const userExists = await checkUser(email);
        console.log('userExists', userExists);
        if (userExists) {
            res.status(400).json('User with this email already exists. Please sign in.');
        } else {
            pool.query(
                'INSERT INTO user_info (firstname, lastname, email) VALUES ($1, $2, $3)',
                [given_name, family_name, email],
                (error, result) => {
                    if (error) {
                        console.error(error); // Log the actual database error for better diagnostics
                        res.status(500).send('Error creating user');
                    } else {
                        res.status(200).send('User created successfully');
                    }
                }
            );
        }
    } catch (error) {
        console.error(error);
        res.status(500).send('Error checking user existence');
    }
});

async function checkUser(email) {
    //const { rowCount } = await pool.query('SELECT COUNT(*) FROM user_info WHERE email = $1', [email]);
    //console.log('rowCount', rowCount);
    const { rows } = await pool.query('SELECT * FROM user_info WHERE email = $1', [email]);
    console.log('User info:', rows);
    return rows.length > 0;
}

app.get('/checkUser', (req, res) => {
    const { email } = req.query; 
    console.log('Incoming data:', {email});

    pool.query(
        'SELECT * FROM user_info WHERE email = $1',
        [email],
        (error, result) => {
            if (error) {
                console.error(error);
                res.status(500).send('Error checking user');
            } else {
                
                    // If the user exists, create a token
                    const userObject = { email }; // Add any other user data you want in the token
                    console.log('userob:', userObject);
                    const exp = Math.floor(Date.now() / 1000) + 60 * 60 * 24; // 1 day
                    const token = jwt.sign({ user: userObject, exp }, 'MIICXQIBAAKBgQDTgFK98zO+ZFLgI6nNw+b7pD1tgqMtaVps7ULZx4wLdbjglmE2Juk1lU4add8ih0g5u6dVXhMdlejiuKxOt4b/0gAigu7iQKXlYu5ic7cmoCjwx+OWEoeiyu6YHr8acg9hj66+748r4EzfJGzBAIxb1hJxeCXHUnHOEtzll0eN9QIDAQABAoGBALydKqzlD1cSRupGQ68RrpLpZDKeFwFve8m6SSzIDPdHU8lNsoHFb6JudQmZ5pT3SgzacZ7q12dCAj72bAuDFeq8+clhWG2GFJxQWczX0Gqk+KHCooGAorCoxVZNIbHS3YOQ8Id0vCsAsZlmUYoZ8KtjpGfBFdyyGs3Jj9v3xUrBAkEA7LEAKM0bzhL9M3YCDc2Zq27bncJRSn4iH7rURhNY/wan8lbe9qUrfmnlwDP9pZkHqWD6NklK221zN3Iy/UtscQJBAOTBQiWzsoG4TsLEQhAHYu0m/0etcnqw4aKjkscILGS+k0t1qszSBEklCkXpPkz2EKKXWpP6cpeU3dK0xeb4S8UCQQDZ2nycEVVzUpUM5aQ0UjYLzYiEZxNtbjU4YTz6ltpGOTkh3AVynUowG4ZlZzUiU3zy0JjcmI828kGnGgyGiQJxAkACRpnt3hfMipTeAy3VEv289kJb6DHXXqMgBxiSulYWun6kpYsJdp1sTN4JTAS+p0QLGg5gooE5WNXMHthJL/cxAkBQzYC0DqR6lO7/hCqzS+SNY3y2p1u1KqBW92GfuHP8vIS1zg34j9LjSsF9U/cZl22GEX9pSXQIeEPijucZUUuS'); // Use a secure secret key
                    console.log('Token created:', token);
                    res.status(200).json({ token }); // Send the token as a JSON response
                } 
        }
    );

});



app.post('/getAgentName', async (req, res) => {
    const { email } = req.body; // The logged-in user's email

    try {
        console.log('email', email);
        const userDetails = await getUserDetails(email);
        

        /*if (userDetails) {
            // Check if userDetails is in the expected format
            if (userDetails.hasOwnProperty('name')) {
                res.status(200).json({ name: userDetails.name });
            } else {
                console.error('Invalid userDetails format:', userDetails);
                res.status(500).send('User details format is invalid');
            } */

        if (userDetails && Array.isArray(userDetails)) {
            const names = userDetails.map((user) => user.name);
            console.log('names', names);
            res.status(200).json({ names }); // Sending an array of names
        } else if (userDetails && userDetails.hasOwnProperty('name')) {
            res.status(200).json({ name: userDetails.name });
        }    
        else {
            console.error('User details not found');
            res.status(404).send('User details not found');
        }
    } catch (error) {
        console.error(error);
        res.status(500).send('Error fetching user details');
    }
});

async function getUserDetails(email) {
    const { rows } = await pool.query('SELECT name FROM user_agents_info WHERE personemail = $1', [email]);
    return rows;
}

app.post('/getAgentAge', async (req, res) => {
    const { email } = req.body; // The logged-in user's email

    

    try {
        const userAge = await getUserAge(email);

        if (userAge && Array.isArray(userAge)) {
            const ages = userAge.map((user) => user.age);
            console.log('ages', ages);
            res.status(200).json({ ages }); // Sending an array of names
        } else if (userAge && userAge.hasOwnProperty('age')) {
            res.status(200).json({ age: userAge.age });
        }    
        else {
            console.error('User details not found');
            res.status(404).send('User details not found');
        }
        /*if (userAge) {
            res.status(200).json({ age: userAge.age });
        } else {
            res.status(404).send('User details not found');
        } */
    } catch (error) {
        console.error(error);
        res.status(500).send('Error fetching user age');
    }
});

async function getUserAge(email) {
    const { rows } = await pool.query('SELECT age FROM user_agents_info WHERE personemail = $1', [email]);
    return rows;
}

app.post('/getAgentPic', async (req, res) => {
  const { email } = req.body; // The logged-in user's email


  try {
      const userPic = await getPic(email);
      console.log('userPic', userPic);

      if (userPic && Array.isArray(userPic)) {
          const pics = userPic.map((user) => user.profile_picture);
          console.log('pics', pics);
          res.status(200).json({ pics }); // Sending an array of names
      } else if (userPic && userPic.hasOwnProperty('profile_picture')) {
          res.status(200).json({ pic: userPic.profile_picture });
      }    
      else {
          console.error('User details not found');
          res.status(404).send('User details not found');
      }
      /*if (userAge) {
          res.status(200).json({ age: userAge.age });
      } else {
          res.status(404).send('User details not found');
      } */
  } catch (error) {
      console.error(error);
      res.status(500).send('Error fetching picture');
  }
});

async function getPic(email) {
  const { rows } = await pool.query('SELECT profile_picture FROM user_agents_info WHERE personemail = $1', [email]);
  return rows;
}

app.post('/getAgentDesc', async (req, res) => {
  const { email } = req.body; // The logged-in user's email

  try {
      const userDesc = await getUserDesc(email);

      if (userDesc && Array.isArray(userDesc)) {
          const descs = userDesc.map((user) => user.user_description);
          console.log('descriptions', descs);
          res.status(200).json({ descs }); // Sending an array of names
      } else if (userDesc && userDesc.hasOwnProperty('user_description')) {
          res.status(200).json({ desc: userDesc.user_description });
      }    
      else {
          console.error('User details not found');
          res.status(404).send('User details not found');
      }
      /*if (userAge) {
          res.status(200).json({ age: userAge.age });
      } else {
          res.status(404).send('User details not found');
      } */
  } catch (error) {
      console.error(error);
      res.status(500).send('Error fetching user desciption');
  }
});

async function getUserDesc(email) {
  const { rows } = await pool.query('SELECT user_description FROM user_agents_info WHERE personemail = $1', [email]);
  return rows;
}

app.post('/getAgentGender', async (req, res) => {
  const { email } = req.body; // The logged-in user's email

  try {
      const userGender = await getUserGender(email);

      if (userGender && Array.isArray(userGender)) {
          const genders = userGender.map((user) => user.gender);
          console.log('genders', genders);
          res.status(200).json({ genders }); // Sending an array of names
      } else if (userGender && userGender.hasOwnProperty('gender')) {
          res.status(200).json({ gender: userGender.gender });
      }    
      else {
          console.error('User genders not found');
          res.status(404).send('User genders not found');
      }
      /*if (userAge) {
          res.status(200).json({ age: userAge.age });
      } else {
          res.status(404).send('User details not found');
      } */
  } catch (error) {
      console.error(error);
      res.status(500).send('Error fetching gender');
  }
});

async function getUserGender(email) {
  const { rows } = await pool.query('SELECT gender FROM user_agents_info WHERE personemail = $1', [email]);
  return rows;
}

app.post('/updateProfilePicture', (req, res) => {
  const { name, profile_picture } = req.body;
  console.log('Incoming pic data:', name, profile_picture);

  pool.query('UPDATE user_agents_info SET profile_picture = $1 WHERE name = $2', [profile_picture, name], (error, results) => {
    if (error) {
        res.status(500).send('Error updating profile picture');
    } else {
        res.status(200).send('Profile picture updated successfully');
    }
  });
});

app.post('/getAgentLastInterview', async (req, res) => {
  const { email } = req.body; // The logged-in user's email

  try {
      const userLastInterview = await getUserInterview(email);

      if (userLastInterview && Array.isArray(userLastInterview)) {
          const days = userLastInterview.map((user) => user.last_chatted);
          console.log('last interviewed days', days);
          res.status(200).json({ days }); // Sending an array of names
      } else if (userLastInterview && userLastInterview.hasOwnProperty('last_chatted')) {
          res.status(200).json({ day: userLastInterview.last_chatted });
      }    
      else {
          console.error('User interview days not found');
          res.status(404).send('User interview days not found');
      }
      /*if (userAge) {
          res.status(200).json({ age: userAge.age });
      } else {
          res.status(404).send('User details not found');
      } */
  } catch (error) {
      console.error(error);
      res.status(500).send('Error fetching user interview day');
  }
});

async function getUserInterview(email) {
  const { rows } = await pool.query('SELECT last_chatted FROM user_agents_info WHERE personemail = $1', [email]);
  return rows;
}

app.post('/getAgentJob', async (req, res) => {
  const { email } = req.body; // The logged-in user's email

  try {
      const useJob = await getUserJob(email);

      if (useJob && Array.isArray(useJob)) {
          const jobs = useJob.map((user) => user.job);
          console.log('jobs', jobs);
          res.status(200).json({ jobs }); // Sending an array of names
      } else if (useJob && useJob.hasOwnProperty('job')) {
          res.status(200).json({ day: useJob.job });
      }    
      else {
          console.error('User jobs not found');
          res.status(404).send('User jobs not found');
      }
      /*if (userAge) {
          res.status(200).json({ age: userAge.age });
      } else {
          res.status(404).send('User details not found');
      } */
  } catch (error) {
      console.error(error);
      res.status(500).send('Error fetching user job');
  }
});

async function getUserJob(email) {
  const { rows } = await pool.query('SELECT job FROM user_agents_info WHERE personemail = $1', [email]);
  return rows;
}



app.post('/updateChatHistory', async (req, res) => {
    const { name, personEmail, conversation } = req.body;

    console.log('Incoming data chat:', name, personEmail, conversation);
  
    try {
      const updateQuery = `UPDATE user_agents_info SET chat_history = $1 WHERE name = $2 AND personemail = $3`;
      const result = await pool.query(updateQuery, [JSON.stringify(conversation), name, personEmail]);

      if (result.rowCount > 0) {
          // Fetch the updated chat history after the update
          const fetchQuery = `SELECT chat_history FROM user_agents_info WHERE name = $1 AND personemail = $2`;
          const fetchResult = await pool.query(fetchQuery, [name, personEmail]);

          if (fetchResult.rows.length > 0) {
            const chatHistory = JSON.parse(fetchResult.rows[0].chat_history);
            res.status(200).send({ message: 'Chat history updated successfully', chatHistory });
          } else {
              res.status(404).send('No rows found after update');
          }
      } else {
          res.status(404).json('No rows updated');
      }
  } catch (error) {
      res.status(500).json('An error occurred while updating chat history');
  }
});

app.post('/getConversation', async (req, res) => {
  const { name, personEmail } = req.body;

  try {
    const { rows } = await pool.query('SELECT chat_history FROM user_agents_info WHERE name = $1 AND personemail = $2', [name, personEmail]);

    if (rows.length > 0) {
      console.log('Fetched conversation:', rows[0].chat_history);
      res.status(200).json({ messages: JSON.parse(rows[0].chat_history) });
    } else {
      console.log('No conversation found for:', name, personEmail);
      res.status(404).json({ message: 'No conversation found' });
    }
  } catch (error) {
    console.error('Error fetching conversation from the database:', error);
    res.status(500).json({ message: 'Error fetching conversation from the database' });
  }
});

  app.get('/check-rows', async (req, res) => {
    const { personEmail } = req.query;
    console.log('personEmailpopup', personEmail);
  
    try {
      const query = 'SELECT COUNT(*) AS rowCount FROM user_agents_info WHERE personemail = $1';
      const result = await pool.query(query, [personEmail]);

      console.log('result', result);
      
      const rowCount = result.rows[0].rowcount;
      console.log('rowCount', rowCount);
  
      res.json({ rowCount });
    } catch (error) {
      res.status(500).json({ error: 'Error occurred while fetching row count' });
    }
  });

  //old
  app.post('/add-persona', async (req, res) => {
    const { age, occupation, description, personEmail } = req.body;
  
    try {
      const query = `
        INSERT INTO user_agents_info (personemail, age, job, user_description)
        VALUES ($1, $2, $3, $4)
      `;
      await pool.query(query, [personEmail, age, occupation, description]);
      
      res.status(200).json({ message: 'Persona added successfully' });
    } catch (error) {
      res.status(500).json({ error: 'Error occurred while adding persona' });
    }
  });

  app.post('/add-persona', async (req, res) => {
    const { age, occupation, description, personEmail } = req.body;
  
    try {
      const query = `
        INSERT INTO user_agents_info (personemail, age, job, user_description)
        VALUES ($1, $2, $3, $4)
      `;
      await pool.query(query, [personEmail, age, occupation, description]);
      
      res.status(200).json({ message: 'Persona added successfully' });
    } catch (error) {
      res.status(500).json({ error: 'Error occurred while adding persona' });
    }
  });

  app.post('/add-report', async (req, res) => {
    const { report, name, personEmail } = req.body;
  
    try {
      const query = `
        UPDATE user_agents_info SET report = $1 WHERE name = $2 AND personemail = $3`;
      await pool.query(query, [report, name, personEmail]);
      
      res.status(200).json({ message: 'Report added successfully' });
    } catch (error) {
        console.error('Error adding report to PostgreSQL:', error);
      res.status(500).json({ error: 'Error occurred while adding report' });
    }
  });

  app.post('/get-report', async (req, res) => {
    const { name, personEmail } = req.body;
  
    try {
      const { rows } = await pool.query('SELECT report FROM user_agents_info WHERE name = $1 AND personemail = $2', [name, personEmail]);
  
      if (rows.length > 0) {
        console.log('Fetched report:', rows[0].report);
        res.status(200).json(rows[0].report );
      } else {
        console.log('No report found for:', name, personEmail);
        res.status(404).json({ report: 'No report found' });
      }
    } catch (error) {
      console.error('Error fetching conversation from the database:', error);
      res.status(500).json({ report: 'Error fetching conversation from the database' });
    }
  });

  app.get('/check-reports', async (req, res) => {
    const { personEmail } = req.query;
    console.log('personEmailpopup', personEmail);
  
    try {
      const query = 'SELECT report FROM user_agents_info WHERE personemail = $1';
      const reports = await pool.query(query, [personEmail]);

      if (reports && Array.isArray(reports)) {
        const hasReportsArray = reports.map(report => report.report !== null && report.report !== undefined);
        res.status(200).json({ hasReports: hasReportsArray });
    } else if (reports && reports.length === 1 && reports[0].hasOwnProperty('report')) {
        // Scenario 2: One row (a single report)
        const hasReport = reports[0].report !== null && reports[0].report !== undefined;
        res.status(200).json({ hasReport });
    } else {
        console.error('Reports not found');
        res.status(404).send('Reports not found');
    }

    } catch (error) {
      res.status(500).json({ error: 'Error occurred while fetching row count' });
    }
  });



  

  app.listen(port, () => {
    console.log("app is listening at http://%s:%s", port);
  });
  
  app.get('*', (req, res) => {
    console.log('Redirecting to index.html at end');
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
  });