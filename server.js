const io = require("socket.io-client");

const socket = io("ws://172.30.1.60:4001/all", {
    reconnection: true,
    reconnectionDelay: 1000,
    timeout: 5000,
});
const dd = ()=>{
    const now = new Date();

    const formatTwoDigits = (n) => n.toString().padStart(2, '0');

    const formatted = [
    formatTwoDigits(now.getFullYear() % 100),  // 년도 두 자리
    formatTwoDigits(now.getMonth() + 1),       // 월 (0부터 시작하므로 +1)
    formatTwoDigits(now.getDate()),            // 일
    formatTwoDigits(now.getHours()),           // 시
    formatTwoDigits(now.getMinutes()),         // 분
    formatTwoDigits(now.getSeconds())          // 초
    ].join('');

    console.log(formatted);  // 예: 250522142912

};
dd();
socket.on("connect", ()=>{
    console.log("connect");
    const a = setInterval(()=>{
        socket.emit("event", {
            "channel":3,
            "status":"제품 투입 감지",
            "time":"250522142912"
        });
    }, 10000);
    socket.on("disconnect", ()=>{
        console.log("disconnect");
        clearInterval(a);
    });
});