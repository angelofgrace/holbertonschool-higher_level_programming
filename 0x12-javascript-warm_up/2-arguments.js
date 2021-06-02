#!/usr/bin/node
// print a message based on the number of arguments passed into script
if (process.argv.length === 2) {
  console.log('No argument');
  process.exit();
} else if (process.argv.length === 3) {
  console.log('Argument found');
  process.exit();
} else {
  console.log('Arguments found');
  process.exit();
}
