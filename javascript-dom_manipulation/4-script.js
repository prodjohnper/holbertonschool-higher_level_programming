/*
  4-script.js

  Script that adds a <li> element to a list when the user clicks on the element with id add_item.
*/

// Adds a <li> element to the list when the tag with id `add_item` is clicked
document.addEventListener('DOMContentLoaded', function () {
  document.getElementById('add_item').addEventListener('click', function () {
    const item = document.createElement('li');
    item.appendChild(document.createTextNode('Item'));
    document.querySelector('ul.my_list').appendChild(item);
  });
});
