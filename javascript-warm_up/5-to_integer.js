#!/usr/bin/node
const arg1asnum = Number(process.argv[2]);
if (!isNaN(arg1asnum)) {
  console.log('My number:', arg1asnum);
} else {
  console.log('Not a number');
}
