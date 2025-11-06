#!/usr/bin/node

const { argv } = require('node:process');

const uni = [...new Set(argv)];
uni.sort((a, b) => b - a);

if (argv.length === 2 || argv.length === 3) {
  console.log(0);
} else {
  console.log(uni[3]);
}
