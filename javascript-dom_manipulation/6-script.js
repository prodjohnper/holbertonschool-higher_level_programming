/*
  6-script.js

  Script that fetches the character name from this
  URL: `https://swapi-api.hbtn.io/api/people/5/?format=json`.
*/

// Fetch the character name from the URL and display it in the HTML tag div with `character` id
document.addEventListener('DOMContentLoaded', function () {
  // Fetch the character name from the URL
  fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
    // Parse the response as JSON
    .then(response => response.json())
    .then(data => {
      // Display the character name in the HTML tag div with `character` id
      const name = data.name;
      document.getElementById('character').textContent = name;
    })
  // Log any errors to the console
    .catch(error => console.log(error.message));
});
