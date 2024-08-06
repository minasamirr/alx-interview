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
            console.error(`Error fetching data: ${err.message}`);
            process.exit(1);
        }

        const charactersUrls = body.characters;

        // Fetch and print each character's name
        let remaining = charactersUrls.length;
        if (remaining === 0) {
            process.exit(0);
        }

        charactersUrls.forEach(characterUrl => {
            request(characterUrl, { json: true }, (err, res, body) => {
                if (err) {
                    console.error(`Error fetching character data: ${err.message}`);
                    process.exit(1);
                }
                
                console.log(body.name);

                remaining--;
                if (remaining === 0) {
                    process.exit(0);
                }
            });
        });
    });
}

getStarWarsCharacters(movieId);
