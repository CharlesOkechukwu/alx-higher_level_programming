#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
let count = 0;

request.get(url, function (error, response, body) {
  if (!error) {
    const res = JSON.parse(body);
    const result = res.results;
    for (let i = 0; i < result.length; ++i) {
      const roles = result[i].characters;
      for (let j = 0; j < roles.length; ++j) {
        const role = roles[j];
        const id = role.split('/')[5];
        if (id === '18') {
          count += 1;
        }
      }
    }
  }
  console.log(count);
});
