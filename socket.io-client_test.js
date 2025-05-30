// const { Server } = require("socket.io");
// const http = require("http");

// const server = http.createServer();
// const io = new Server(server, {
//   cors: {
//     origin: "*"
//   }
// });

// io.of("/chat").on("connection", (socket) => {
//   console.log("클라이언트 연결됨: ", socket.id);

//   socket.on("message", (data) => {
//     console.log("받은 메시지: ", data);
//     socket.emit("reply", `서버가 받은 메시지: ${data}`);
//   });
// });

// server.listen(3000, () => {
//   console.log("서버 실행 중: http://localhost:3000");
// });

const io = require("socket.io-client");

// "/chat" 네임스페이스에 연결
const socket = io("http://localhost:3000/chat");

// 연결 성공 시
socket.on("connect", () => {
  console.log("서버에 연결됨:", socket.id);

  // 서버에 메시지 전송
  socket.emit("message", "안녕하세요, 서버님!");

  // 서버로부터 응답 수신
  socket.on("reply", (data) => {
    console.log("서버 응답:", data);
  });
});

// 연결 종료 시
socket.on("disconnect", () => {
  console.log("서버 연결 종료됨");
});


console.log("whatwhat")
socket.emit("message", "안녕하세요, 서버님!");
console.log("whatwhat")
