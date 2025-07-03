const { Server } = require("socket.io");
const http = require("http");

const app = http.createServer();
const io = new Server(app, {
    cors: {
        origin: "*", // 원격 연결 허용 (원하는 도메인으로 수정 가능)
    },
});

app.listen(4003, () => {
    console.log("Server is running on port 4003");
});

// /output 네임스페이스에서 클라이언트 연결을 처리
const outputNamespace = io.of("/output");

outputNamespace.on("connection", (socket) => {
    console.log("Client connected to /output namespace: ", socket.id);

    // 클라이언트로부터 메시지를 받았을 때 처리
    socket.on("message", (data) => {
        console.log("Received message:", data);
    });

    socket.on("disconnect", () => {
        console.log("Client disconnected from /output namespace");
    });
});

// 클라이언트 연결 실패 시 자동 재연결 처리 (서버 측에서 처리)
outputNamespace.on("connect_error", (error) => {
    console.log("Error connecting to /output namespace:", error);
    // 자동으로 재연결을 시도하려면, 재연결 로직을 구현할 수 있습니다.
});

// 서버가 /output 네임스페이스에 연결된 클라이언트에게 메시지 보내기
setInterval(() => {
    outputNamespace.emit("message", "Hello from server!");
}, 5000); // 5초마다 클라이언트에게 메시지 발송
