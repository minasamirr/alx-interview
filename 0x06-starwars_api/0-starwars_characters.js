#!/usr/bin/node
const request = require('request');
const API_URL = 'https://swapi-api.hbtn.io/api';
const movieId = process.argv[2];

if (!movieId) {
  request(`${API_URL}/films/${movieId}/`, (err, _, body) => {
    if (err)
      console.log(err);
    const charactersName = JSON.parse(body).characters.map(
      url => new Promise((resolve, reject) => {
        request(url, (promiseError, __, promiseBody) => {
          promiseError ? reject(promiseError) : resolve(JSON.parse(promiseBody).name);
        });
      }));

    Promise.all(charactersName)
      .then(names => console.log(names.join('\n')))
      .catch(allErr => console.log(allErr));
  });
}
