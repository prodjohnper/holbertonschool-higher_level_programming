/*
  5-script.js

  Script that updates the text of the header element to `New Header!!!`
  when the user clicks on the element with id update_header.
*/

// Update the text of the header element to `New Header!!!` when the tag with id `update_header` is clicked
document.addEventListener('DOMContentLoaded', function () {
  document.getElementById('update_header').addEventListener('click', function () {
    document.querySelector('header').textContent = 'New Header!!!';
  });
});
