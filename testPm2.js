const express = require("express");
const app = express();
app.get("/", (req,res)=>{res.send("TEST")});
app.listen(5010, ()=>{console.log("run")});