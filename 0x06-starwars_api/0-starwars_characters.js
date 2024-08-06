#!/usr/bin/env node

const request = require('request-promise');
const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

async function getStarWarsCharacters (movieId) {
  const baseUrl = 'https://swapi.dev/api/films/';
  const url = `${baseUrl}${movieId}/`;

  try {
    // Fetch film data
    const filmData = await request({ uri: url, json: true });

    // Get character URLs
    const charactersUrls = filmData.characters;

    // Fetch and print each character's name
    for (const characterUrl of charactersUrls) {
      const charData = await request({ uri: characterUrl, json: true });
      console.log(charData.name);
    }
  } catch (error) {
    console.error(`Error fetching data: ${error.message}`);
    process.exit(1);
  }
}

getStarWarsCharacters(movieId);
