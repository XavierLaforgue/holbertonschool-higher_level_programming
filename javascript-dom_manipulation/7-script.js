#!/usr/bin/node
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
const listMovies = document.querySelector('#list_movies');
fetch(url)
  .then(response => response.json())
  .then(titleList => {
    const ListOfTitles = titleList.results.map(film => film.title);
    ListOfTitles.forEach(title => {
      const newTitle = document.createElement('li');
      newTitle.textContent = title;
      listMovies.append(newTitle);
    });
  });
