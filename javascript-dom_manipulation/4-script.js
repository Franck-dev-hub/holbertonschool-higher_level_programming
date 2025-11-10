function addItems () {
  const newItem = document.createElement('li');
  newItem.textContent = 'Item';
  document.querySelector('ul.my_list').appendChild(newItem);
}

document.getElementById('add_item').addEventListener('click', addItems);
