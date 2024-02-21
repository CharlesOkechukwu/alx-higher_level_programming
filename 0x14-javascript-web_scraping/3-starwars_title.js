#!/usr/bin/node

const request = require('request');
const source = 'https://swapi-api.alx-tools.com/api/films/:id'.concat(process.argv[2]);
request.get(source, function (error, response, body) {
  if (!error) {
    console.log(JSON.parse(body).title);
  }
});
