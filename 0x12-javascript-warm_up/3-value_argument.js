#!/usr/bin/node
// print the value of the first cmd line arg passed

if (process.argv[2]) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
