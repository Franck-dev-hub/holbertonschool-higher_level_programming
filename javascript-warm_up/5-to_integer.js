#!/usr/bin/node

const { argv } = require('node:process');

if (argv.length > 2) {
  const num = Number(argv[2]);
  if (!isNaN(num)) {
    console.log('My number:', num);
  } else {
    console.log('Not a number');
  }
}
