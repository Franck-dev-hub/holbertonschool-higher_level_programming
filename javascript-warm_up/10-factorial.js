#!/usr/bin/node

const { argv } = require('node:process');

function factorial (a) {
  if (isNaN(a) || a < 0) return NaN;
  let result = 1;
  for (let i = 2; i <= a; i++) {
    result = result * i;
  }
  return result;
}

if (argv.length > 2) {
  const num = Number(argv[2]);
  console.log(factorial(num));
} else {
  console.log(1);
}
