const express = require('express');
const path = require('path');
const app = express();
const PORT = 5020;

// public 폴더 내 정적 파일 제공
app.use(express.static(path.join(__dirname, 'tests', 'build')));

// 루트로 접속 시 index.html 제공
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'tests/build/index.html'));
});

app.listen(PORT, () => {
  console.log(`서버 실행 중: http://localhost:${PORT}`);
});
