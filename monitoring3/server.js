// 송출 화면 조회
const express = require('express');
const http = require('http');
const { Server } = require('socket.io');
const app = express();
const server = http.createServer(app);
const io = new Server(server, {
  cors:{
    origin: "*",
  }
});

let connected_clients = 0;
io.on('connection', socket => {
  connected_clients++;
  console.log(`connected -> number of clients: ${connected_clients}`);

  socket.on('disconnect', socket=>{
    connected_clients--;
    console.log(`disconnected -> number of clients: ${connected_clients}`);
  })

  socket.on('screen', (data)=>{
    io.emit('screen', data);
  });
});


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
        <script src="/socket.io/socket.io.js"></script>
        <script>
          const socket = io();
          socket.on('screen', data => {
            const blob = new Blob([data], { type: 'image/jpeg' });
            document.getElementById('screen').src = URL.createObjectURL(blob);
          });
        </script>
      </body>
    </html>
  `);
});


const port = 5011;
server.listen(port, () => {
  console.log(`Server on http://localhost:${port}`);
});

