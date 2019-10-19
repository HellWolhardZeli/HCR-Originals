const http = require('http');
const express = require('express');
const hostname = '192.168.1.121';
const port = 4000;

const server = http.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hello World\n');
});

var port = process.env.port || 3000;

server.listen(port);
