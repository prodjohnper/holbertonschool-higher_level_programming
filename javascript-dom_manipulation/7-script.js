/*
  7-script.js

  Script that fetches and lists the title for all movies by using
  this URL: `https://swapi-api.hbtn.io/api/films/?format=json`.
*/

// Fetch the URL and display the titles of the movies
document.addEventListener('DOMContentLoaded', function () {
  // Fetch the URL
  fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    // Parse the response as JSON
    .then(response => response.json())
    .then(data => {
      // Display the titles of the movies in the HTML tag ul with `list_movies` id
      for (const movie of data.results) {
        // Create a new list item element and append the movie title to it
        const item = document.createElement('li');
        item.appendChild(document.createTextNode(movie.title));
        document.querySelector('ul#list_movies').appendChild(item);
      }
    });
});
