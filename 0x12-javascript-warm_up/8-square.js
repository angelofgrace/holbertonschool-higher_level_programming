#!/usr/bin/node
// print a square of a given size

if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let len = 0; len < process.argv[2]; len++) {
    let str = '';
    for (let wid = 0; wid < process.argv[2]; wid++) {
      str = str.concat('X');
    }
  console.log(str);
  }
}
