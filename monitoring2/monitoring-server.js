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
const screenshot = require('screenshot-desktop');

let connected_clients = 0;
io.on('connection', socket => {
  connected_clients++;
  console.log(`connected -> number of clients: ${connected_clients}`);
  socket.on('disconnect', socket=>{
    connected_clients--;
    console.log(`disconnected -> number of clients: ${connected_clients}`);
  })
});

setInterval(async()=>{
  if(connected_clients!==0){
    // console.log("my_debug");
    try {
      const img = await screenshot({ format: 'png' });
      io.emit('screen', img);
    } catch (e) {
      console.error('캡처 실패:', e);
    }
  }
}, 250);


const port = 5011;
server.listen(port, () => {
  console.log(`Server on http://localhost:${port}`);
});

