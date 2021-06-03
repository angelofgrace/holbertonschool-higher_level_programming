#!/usr/bin/node
// search a list of integers for the second largest among them

if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(0);
} else {
  let max = -Infinity;
  let result = -Infinity;
  let x = 2;
  while (process.argv[x]) {
    const num = parseInt(process.argv[x]);
    if (num > max) {
      [result, max] = [max, num];
    } else if (num < max && num > result) {
      result = num;
    }
    x++;
  }
  console.log(result);
}
