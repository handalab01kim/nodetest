const express = require('express');
const http = require('http');
const { Server } = require('socket.io');
const app = express();
const server = http.createServer(app);
const io = new Server(server);

let latestImage = null;

io.on('connection', socket => {
  console.log('agent connected');

  socket.on('screen', (data) => {
    // console.log("got");
    latestImage = data;
    io.emit('broadcast', data); // 다른 클라이언트(브라우저)에게 전달
  });
});

app.get('/', (req, res) => {
//   res.send(`
//     <html><body>test
//       <img id="screen" width="800"/>
//       <script src="/socket.io/socket.io.js"></script>
//       <script>
//         const socket = io();
//         socket.on('broadcast', data => {
//           const blob = new Blob([data], { type: 'image/jpeg' });
//           document.getElementById('screen').src = URL.createObjectURL(blob);
//         });
//       </script>
//     </body></html>
//   `);
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
        socket.on('broadcast', data => {
          const blob = new Blob([data], { type: 'image/jpeg' });
          document.getElementById('screen').src = URL.createObjectURL(blob);
        });
      </script>
    </body>
  </html>
    `);
});

server.listen(5011, () => {
  console.log('Server on http://localhost:5011');
});
