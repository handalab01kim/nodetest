const io = require('socket.io-client');
const express = require('express');
const app = express();

const serverUrl = "http://localhost:5011";
app.get('/', (req, res) => {
  res.send(`
    <html>
      <head>
        <style>
          body, html {
            margin: 0;
            padding: 0;
            overflow: hidden;
          }
          #screen {
            width: 100vw;
            height: auto;
            display: block;
          }
        </style>
      </head>
      <body>
        <img id="screen" />
        <script src="${serverUrl}/socket.io/socket.io.js"></script>
        <script>
          const socket = io("${serverUrl}");
          socket.on('screen', data => {
            const blob = new Blob([data], { type: 'image/jpeg' });
            document.getElementById('screen').src = URL.createObjectURL(blob);
          });
        </script>
      </body>
    </html>
  `);
});


const port = 5012;
app.listen(port, () => {
  console.log(`Server on http://localhost:${port}`);
});

//npm install screenshot-desktop socket.io socket.io-client express
