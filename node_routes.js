const express = require('express');
const router = express.Router();

// Define your Node.js specific routes
router.get('/node', (req, res) => {
    res.send('Hello from Node.js!');
});

module.exports = router;
