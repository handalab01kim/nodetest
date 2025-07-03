const express = require('express');
const app = express();
const port = 8999;

app.get('/', (req, res) => {
    console.log("TEST");
    res.send('Hello World!');
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
