const io = require('socket.io-client');
const screenshot = require('screenshot-desktop');
const socket = io('http://172.30.1.88:5011');

setInterval(async () => {
  try {
    const img = await screenshot({ format: 'png' });
    socket.emit('screen', img);
  } catch (e) {
    console.error('캡처 실패:', e);
  }
}, 500);

//npm install screenshot-desktop socket.io socket.io-client express
