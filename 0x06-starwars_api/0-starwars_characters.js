#!/usr/bin/node
const request = require('request');

// Check if a movie ID was provided as an argument
if (process.argv.length !== 3) {
  console.log('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;

// Fetch the movie data from the Star Wars API
request(url, (error, response, body) => {
  if (error) {
    console.error('Error fetching data:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('Failed to fetch data:', response.statusCode);
    process.exit(1);
  }

  const filmData = JSON.parse(body);

  // Extract character URLs
  const characterUrls = filmData.characters;

  // Fetch and print each character's name
  characterUrls.forEach(characterUrl => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error('Error fetching character data:', error);
        return;
      }

      if (response.statusCode !== 200) {
        console.error('Failed to fetch character data:', response.statusCode);
        return;
      }

      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});

