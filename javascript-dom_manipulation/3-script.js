function toggleColor () {
  const header = document.querySelector('header');
  header.classList.toggle('red');
  header.classList.toggle('green');
}

document.getElementById('toggle_header').addEventListener('click', toggleColor);
