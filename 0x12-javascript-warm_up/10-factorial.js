#!/usr/bin/node
// print a factorial using recursion

function f (n) {
  if (isNaN(process.argv[2]) || n === 1) {
    return (1);
  } else {
    return ((n !== 1) ? n * f(n - 1) : 1);
  }
}

console.log(f(process.argv[2]));
