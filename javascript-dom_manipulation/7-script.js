const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

fetch(url)
  .then(response => response.json())
  .then(data => {
    for (let i = 0; i < data.results.length; i++) {
      const newItem = document.createElement('li');
      newItem.innerText = data.results[i].title;
      document.querySelector('ul').appendChild(newItem);
    }
  })
