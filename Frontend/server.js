

const express = require('express');
const fs = require('fs');

const app = express();
app.use(express.json());

app.post('/writefile', function(req, res) {
  const content = req.body.content;

  fs.writeFile('file.txt', content, function(err) {
    if (err) {
      console.error(err);
      res.status(500).send('Errore durante la scrittura del file.');
      return;
    }
    res.sendStatus(200);
  });
});

app.listen(3000, function() {
  console.log('Server avviato sulla porta 3000');
});


//open -n -a /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --args --user-data-dir="/tmp/chrome_dev_test" --disable-web-security
//node server.js
