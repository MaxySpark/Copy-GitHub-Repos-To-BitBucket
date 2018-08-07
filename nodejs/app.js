const express = require('express');
const _ = require("lodash");
const request = require("request");
const config = require('./config/config.js');

request.get('https://api.github.com/user/repos', {
  'auth': {
    'user': config.github.username,
    'pass': config.github.password
  },
  headers: {
    'User-Agent': 'nodejs'
  }
},function(err,res,body){
    console.log(body);
});