import express from 'express';
import bodyParser from 'body-parser';
import https from 'https';
import fs from 'fs';

import cors from 'cors'; 

const app = express();
const PORT = 9876;

app.use(cors());

// JSON 파싱 미들웨어
app.use(bodyParser.json());

// 클라이언트에서 전송된 로그 출력 라우터
app.post('/log', (req, res) => {
    const { message } = req.body;

    if (message) {
        const timestamp = new Date().toISOString();
        console.log(`[CLIENT LOG ${timestamp}]`, message);
    } else {
        console.log('[CLIENT LOG] <Empty message>');
    }

    res.sendStatus(200);
});
/*
client
    const logToServer = (args) => {
        fetch('https://172.30.1.88:9876/log', {
            method: 'POST',
            body: JSON.stringify({ message: args}),
            headers: { 'Content-Type': 'application/json' }
        });
        console.log
    };
*/

// HTTPS 서버 생성
const server = https.createServer(
    {
        key: fs.readFileSync('./key.pem'),
        cert: fs.readFileSync('./cert.pem')
    },
    app
);

// 서버 실행
server.listen(PORT, () => {
    console.log(`🟢 HTTPS log server running at https://localhost:${PORT}`);
});
