// Add element
function add () {
  const newItem = document.createElement('li');
  newItem.textContent = 'Item';
  document.querySelector('.my_list').appendChild(newItem);
}

// Delete last element
function remove () {
  const listItems = document.querySelectorAll('.my_list li');
  if (listItems.length > 0) {
    listItems[listItems.length - 1].remove();
  }
}

// Clear the list
function clear () {
  document.querySelector('.my_list').innerHTML = '';
}

// Wait DOM to be full loaded
document.addEventListener('DOMContentLoaded', function () {
  document.getElementById('add_item').addEventListener('click', add);
  document.getElementById('remove_item').addEventListener('click', remove);
  document.getElementById('clear_list').addEventListener('click', clear);
});
