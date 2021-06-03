#!/usr/bin/node
// change a value pointed to by a constant object

const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

myObject['value'] = 89;

console.log(myObject);
