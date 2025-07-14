#!/usr/bin/node
const Str = 'C is fun';
const x = Number(process.argv[2]);
if (isNaN(x)) {
  console.log('Missing number of occurrences');
}
for (let i = 0; i < x; i++) {
  console.log(Str);
}
