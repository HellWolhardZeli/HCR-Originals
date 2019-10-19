const http = require('http');
var express = require('express');
var app = express();


app.get('/', function (req, res) {
    res.send('<h1>Hello</h1>');
});


const port = process.env.PORT || 1337;
app.listen(port);

console.log("Server running at http://localhost:%d", port);
