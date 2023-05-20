
const express = require('express');
const fs = require('fs');

const app = express();
app.use(express.json());

app.post('/writefile', function(req, res) {
  const content = req.body.content;

  fs.truncate('file.txt', 0, function(err) {
    if (err) {
      console.error(err);
      res.status(500).send('Error truncating file.');
      return;
    }

    fs.writeFile('file.txt', content, function(err) {
      if (err) {
        console.error(err);
        res.status(500).send('Error writing file.');
        return;
      }
      res.sendStatus(200);
    });
  });
});

app.listen(3000, function() {
  console.log('Server running on port 3000');
});


//Linux disable cors
//google-chrome --disable-web-security

//Mac disable cors
//open -n -a /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --args --user-data-dir="/tmp/chrome_dev_test" --disable-web-security

//Run server
//node server.js
