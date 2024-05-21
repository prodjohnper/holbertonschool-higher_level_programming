/*
  8-script.js

  Script that fetches from `https://hellosalut.stefanbohacek.dev/?lang=fr` and
  displays the value of `hello` from that fetch in the HTML element with id `hello`.
*/

// Fetch the URL and parse the JSON response to get the `hello` value from the response
document.addEventListener('DOMContentLoaded', function () {
  // Fetch the URL
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    // Parse the JSON response
    .then(response => {
      // Check if the response is ok
      if (!response.ok) {
        // Throw an error if the response is not ok
        throw new Error('Network response was not ok');
      }
      // Return the JSON response
      return response.json();
    })
    // Get the `hello` value from the response
    .then(data => {
      // Get the `hello` value from the response and display it in the HTML element with id `hello`
      const helloTranslation = data.hello;
      document.getElementById('hello').textContent = helloTranslation;
    })
    // Catch any errors that occur during the fetch
    .catch(error => {
      // Log the error to the console
      console.error('Error fetching translation:', error);
    });
});
