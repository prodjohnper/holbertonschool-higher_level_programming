/*
  2-script.js

  Script that adds the class red to the header element
  when the user clicks on the tag with id red_header.
*/

// Adds the class red when the tag with id `red_header` is clicked
document.addEventListener('DOMContentLoaded', function () {
  document.getElementById('red_header').addEventListener('click', function () {
    document.querySelector('header').classList.add('red');
  });
});
