#!/usr/bin/node
const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
fetch(url)
  .then(response => response.json())
  .then(response2 => {
    const fetchedHello = response2.hello;
    const hello = document.querySelector('#hello');
    hello.textContent = fetchedHello;
  });
