function translate () {
  const language = document.getElementById('language_code').value;
  if (language === '') {
    document.getElementById('hello').textContent = '';
    return;
  }

  const url = `https://hellosalut.stefanbohacek.com/?lang=${language}`;

  fetch(url)
    .then(response => response.json())
    .then(data => {
      document.getElementById('hello').textContent = data.hello;
    })
    .catch(error => console.error('Error:', error));
}

document.addEventListener('DOMContentLoaded', function () {
  document.getElementById('btn_translate').addEventListener('click', translate);
});
