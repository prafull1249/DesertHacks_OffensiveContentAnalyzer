//'use strict';

var express = require('express');
var watson = require('watson-developer-cloud');
var path = process.cwd();
//var authorHandler = require(path + '/app/controllers/authorHandler.server.js');
//var bookHandler = require(path + '/app/controllers/bookHandler.server.js');
var bodyParser = require('body-parser');
//var MongoClient = require('mongodb').MongoClient;

var app = express();
//var watson = require('watson-developer-cloud');
   var alchemy_language = watson.alchemy_language({
  api_key: 'de1dd2eb1487d502de86cf8be3f814dbc721be7c'
});





//if (process.env.NODE_ENV !== 'production') require('dotenv').load();

app.use(bodyParser.json());
//app.use(bodyParser.urlencoded({ extended: true }))
//app.use('/controllers', express.static(process.cwd() + '/app/controllers'));

app.get('/', function(req, res) {


	

  //console.log(req.params['search'])
  console.log("query : ", req.query['search'])
   console.log("Fetch Results")
  //res.send(req.query['search']);
    //getResponse(res , req.query['search'])
  //jsonResult = JSON.stringify(getResponse(), function() {
    console.log("got response")
    

var parameters = {
  extract: 'entities,keywords,doc-emotion, doc-sentiment',
  text: req.query['search']
};

alchemy_language.combined(parameters, function (err, response) {
  if (err)
    console.log('error:', err);
  else
  	var r = JSON.stringify(response)
  console.log(r);
  	res.write(r);
    res.end();
  	//console.log(JSON.stringify(response, null, 2));
});

  
 });
  



//var port = process.env.PORT || 8080;
var port = 8081;

//mongoose.connect('mongodb://localhost/myappdatabase');
//MongoClient.connect("mongodb://localhost/", function(err, db) {  

//var connection = mongoose.connect(process.env.MONGO_URI || process.env.MONGODB_URI);
//var connection = mongoose.connect('mongodb://localhost/');
var server = app.listen(port, function() {
  console.log('Running at port ' + port + '...');
});
