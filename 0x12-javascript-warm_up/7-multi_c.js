#!/usr/bin/node
// print a string x times

if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  let x = process.argv[2];
  let i = 0;
  while (i < x) {
    console.log('C is fun');
    i++
  }
}
