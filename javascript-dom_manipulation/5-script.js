function changeText () {
  document.querySelector('header').textContent = 'New Header!!!';
}

document.getElementById('update_header').addEventListener('click', changeText);
