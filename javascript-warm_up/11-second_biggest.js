#!/usr/bin/node
const IntArray = process.argv.slice(2).map(Number);
let biggest, almostbiggest;
if (IntArray.length === 0 || IntArray.length === 1) {
  console.log(0);
} else {
  console.log(SecondBiggest(IntArray));
}
function SecondBiggest (SomeArray) {
  if (SomeArray[0] > SomeArray[1]) {
    biggest = SomeArray[0];
    almostbiggest = SomeArray[1];
  } else {
    biggest = SomeArray[1];
    almostbiggest = SomeArray[1];
  }
  let i = 2;
  while (i < SomeArray.length) {
    if (SomeArray[i] > biggest) {
      almostbiggest = biggest;
      biggest = SomeArray[i];
    } else if (SomeArray[i] > almostbiggest) {
      almostbiggest = SomeArray[i];
    }
    i++;
  }
  return almostbiggest;
}
