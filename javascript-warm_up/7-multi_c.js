#!/usr/bin/node

const { argv } = require('node:process');

if (argv.length > 2) {
  const num = Number(argv[2]);
  if (!isNaN(num)) {
	  for (let i = 0; i < num; i++) {
		console.log('My number: ', num);
	  }
  } else {
    console.log('Missing number of occurrences');
  }
}
