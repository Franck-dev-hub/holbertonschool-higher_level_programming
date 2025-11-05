#!/usr/bin/node

const { argv } = require('node:process');

function add (a, b) {
  return a + b;
}

if (argv.length === 4) {
  const num1 = Number(argv[2]);
  const num2 = Number(argv[3]);

  if (!isNaN(num1) && !isNaN(num2)) {
    console.log(add(num1, num2));
  } else {
    console.log('NaN');
  }
}
