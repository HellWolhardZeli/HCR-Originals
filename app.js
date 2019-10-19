const http = require('http');
var express = require('express');
var parser = require("body-parser");

var app = express();


app.use(parser.urlencoded({
    extended: true
}));

app.get('/', function (req, res) {
    res.render("index.ejs");
});


const port = process.env.PORT || 1337;
app.listen(port);

console.log("Server running at http://localhost:%d", port);
