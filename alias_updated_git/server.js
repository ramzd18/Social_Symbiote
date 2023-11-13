const express = require('express');
const mysql = require('mysql');
const bodyParser = require('body-parser');
const path = require('path');
const Knex = require('knex');
const fs = require('fs');
const cors = require('cors');
const { Pool } = require('pg');
const jwt = require('jsonwebtoken');


const app = express();
app.use(cors());
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

  app.post('/createUser', (req, res) => {
    const { given_name, family_name, email } = req.body;
    console.log('Incoming data:', given_name, family_name, email);
  
    try {
        const userExists = checkUser(email);
        if (userExists) {
            res.status(400).send('User with this email already exists');
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
    const { rowCount } = await pool.query('SELECT COUNT(*) FROM user_info WHERE email = $1', [email]);
    return rowCount > 0;
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



app.post('/updateChatHistory', async (req, res) => {
    const { name, personEmail, conversation } = req.body;

    console.log('Incoming data chat:', name, personEmail, conversation);
  
    try {
      const updateQuery = `
        UPDATE user_agents_info
        SET chat_history = $1
        WHERE name = $2 AND personemail = $3
      `;
      
      const result = await pool.query(updateQuery, [conversation, name, personEmail]);

      console.log('result', result);
  
      if (result.rowCount > 0) {
        res.status(200).json('Chat history updated successfully');
      } else {
        res.status(404).json('No rows updated');
      }
    } catch (error) {
      res.status(500).json('An error occurred while updating chat history');
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

  app.post('/add-persona', async (req, res) => {
    const { age, occupation, description, personEmail } = req.body;
  
    try {
      const query = `
        INSERT INTO user_agents_info (personemail, age, educationwork, user_description)
        VALUES ($1, $2, $3, $4)
      `;
      await pool.query(query, [personEmail, age, occupation, description]);
      
      res.status(200).json({ message: 'Persona added successfully' });
    } catch (error) {
      res.status(500).json({ error: 'Error occurred while adding persona' });
    }
  });
  
  
  
  app.listen(5432, () => {
    console.log('Server running on port: 5432');
  });

  app.get('*', (req, res) => {
    res.sendFile(path.join('/Users/kanshruti/Documents/GitHub/alias-web/alias_updated_git/public/index.html'));
  });