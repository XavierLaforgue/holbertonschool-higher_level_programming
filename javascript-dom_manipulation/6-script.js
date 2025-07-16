#!/usr/bin/node
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
async function fetchName (url) {
  const response = await fetch(url);
  const responseJson = await response.json();
  return responseJson.name;
}
fetchName(url).then(name => {
  const character = document.querySelector('#character');
  character.append(name);
});
