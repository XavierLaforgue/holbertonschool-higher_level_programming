#!/usr/bin/node
const Size = Number(process.argv[2]);
if (!Number.isInteger(Size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < Size; i++) {
    console.log('X'.repeat(Size));
  }
}
