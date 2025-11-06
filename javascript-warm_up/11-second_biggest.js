#!/usr/bin/node

const { argv } = require('node:process');

function second (argv) {
  const nums = [];
  for (let i = 2; i < argv.length; i++) {
    nums.push(argv[i]);
  }
  return nums.sort().reverse();
}

if (argv.length === 2 || argv.length === 3) {
  console.log(0);
} else {
  console.log(second(argv)[1]);
}
