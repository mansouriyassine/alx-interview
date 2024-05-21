#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

const movieUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(movieUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Error: Invalid response from API');
    return;
  }

  const movieData = JSON.parse(body);
  const characterUrls = movieData.characters;

  const fetchCharacter = (index) => {
    if (index >= characterUrls.length) return;

    request(characterUrls[index], (charError, charResponse, charBody) => {
      if (charError) {
        console.error('Error:', charError);
        return;
      }

      if (charResponse.statusCode !== 200) {
        console.error('Error: Invalid response from API');
        return;
      }

      const characterData = JSON.parse(charBody);
      console.log(characterData.name);
      fetchCharacter(index + 1);
    });
  };

  fetchCharacter(0);
});
