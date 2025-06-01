// 화면 송출
const express = require('express');
const app = express();
const io = require('socket.io-client');
const socket = io('http://172.30.1.88:5011');
const screenshot = require('screenshot-desktop');

let socketInterval;
socket.on('connect', () => {
  socketInterval = setInterval(async()=>{
    // console.log("my_debug");
    try {
      const img = await screenshot({ format: 'png' });
      socket.emit('screen', img);
    } catch (e) {
      console.error('캡처 실패:', e);
    }
  }, 250);
});


socket.on('disconnect', () => {
  clearInterval(socketInterval);
});



const port = 5012;
app.listen(port, () => {
  console.log(`Server on http://localhost:${port}`);
});

//npm install screenshot-desktop socket.io socket.io-client express
