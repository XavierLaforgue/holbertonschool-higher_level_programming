#!/usr/bin/node
const header = document.querySelector('header');
const toggleHeader = document.querySelector('#toggle_header');
toggleHeader.addEventListener('click', () => {
  header.classList.toggle('green');
  header.classList.toggle('red');
  }
);
