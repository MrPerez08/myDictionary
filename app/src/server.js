const express = require('express');
const fs = require('fs');
const cors = require('cors');
const app = express();

app.use(cors()); // Allows your frontend to talk to this server
app.use(express.json()); // Allows server to read JSON data

app.post('/save-words', (req, res) => {
    const newWords = req.body.words;

    // Append the words to your text file
    fs.appendFile('wordcompiler.txt', newWords + '\n', (err) => {
        if (err) {
            console.error(err);
            return res.status(500).send('Error saving file');
        }
        console.log('Words saved to wordcompiler.txt!');
        res.send('Saved successfully');
    });
});

app.listen(3000, () => console.log('Server running on http://localhost:3000'));