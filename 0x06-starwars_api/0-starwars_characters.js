#!/usr/bin/env node

const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
    console.error('Usage: ./0-starwars_characters.js <movie_id>');
    process.exit(1);
}

function getStarWarsCharacters(movieId) {
    const baseUrl = 'https://swapi.dev/api/films/';
    const url = `${baseUrl}${movieId}/`;

    request(url, { json: true }, (err, res, body) => {
        if (err) {
            console.error(err);
        }

        const charactersUrls = JSON.parse(body).characters;
        const charactersName = charactersUrls.map(
          url => new Promise((resolve, reject) => {
            request(url, (promiseError, promiseResquet, promiseBody) => {
              if (promiseError) {
                reject(promiseError);
              }
              resolve(JSON.parse(promiseBody).name);
            });
          }));
    
        Promise.all(charactersName)
          .then(names => console.log(names.join('\n')))
          .catch(allErr => console.log(allErr));
    });
}

getStarWarsCharacters(movieId);
