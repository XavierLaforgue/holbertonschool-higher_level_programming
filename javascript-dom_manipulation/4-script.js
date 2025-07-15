#!/usr/bin/node
const unordList = document.querySelector('.my_list');
const addItem = document.querySelector('#add_item');
addItem.addEventListener('click', () => {
  const newItem = document.createElement('li');
  newItem.textContent = 'Item';
  unordList.append(newItem);
}
);
