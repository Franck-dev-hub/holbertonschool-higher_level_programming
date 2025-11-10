function changeToRed () {
  document.querySelector('header').classList.add('red');
}

document.getElementById('red_header').addEventListener('click', changeToRed);
