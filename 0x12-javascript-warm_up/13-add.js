#!/usr/bin/node
// print the addition of two input integers

function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    console.log('NaN');
  } else {
    const sum = (parseInt(a) + parseInt(b));
    return (sum);
  }
}

// export the simple addition function

exports.add = add;
