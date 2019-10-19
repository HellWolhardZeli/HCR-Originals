const http = require('http');
const express = require('express');


const server = http.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hello World\n');
});

var port = process.env.port || 3000;

server.listen(port);
console.log("Server running at http://localhost:%d", port);
