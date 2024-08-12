#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;

if (movieId) {
  request(url, (error, response, body) => {
    if (error) {
      console.log(error);
    }

    const characterUrls = JSON.parse(body).characters;

    const charNames = characterUrls.map(
      characterUrl => new Promise((resolve, reject) => {
        request(characterUrl, (error, response, body) => {
          if (error) {
            reject(error);
            return;
          }
          resolve(JSON.parse(body).name);
        });
      }));
    Promise.all(charNames)
      .then(name => console.log(name.join('\n')))
      .catch(err => console.log(err));
  });
}
