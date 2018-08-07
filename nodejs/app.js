const express = require('express');
const _ = require("lodash");
const request = require("request");
const config = require('./config/config.js');

request.get('https://api.github.com/user/repos', {
  'auth': {
    'user': config.github.username,
    'pass': config.github.password
  },
  json : true,
  headers: {
    'User-Agent': 'nodejs'
  }
},function(err,res,body){

    let private_repos = _.filter(body,function(repo) { return repo.private === true; });

    let repo_data = [];

    private_repos.forEach(repo => {
      let model = {
        'name'      : repo.name,
        'git_url'   : repo.git_url,
        'ssh_url'   : repo.ssh_url,
        'clone_url' : repo.clone_url
      }
      repo_data.push(model);
    });

    

    console.log(repo_data);
    // body.forEach(element => {
    //   console.log(element);
    // });
    // console.log(typeof(body));
    // console.log(JSON.parse(body));
});