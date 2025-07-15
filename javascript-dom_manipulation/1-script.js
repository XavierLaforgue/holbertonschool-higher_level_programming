#!/usr/bin/node
const header = document.querySelector('header');
const tag = document.querySelector('#red_header');
tag.addEventListener('click',
  function colorRed () {
    header.style.color = 'red';
  }
);
