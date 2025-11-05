#!/usr/bin/node

const { argv } = require('node:process');

if (argv.length > 2) {
  const num = Number(argv[2]);
  if (!isNaN(num)) {
    for (let i = 0; i < num; i++) {
      for (let j = 0; j < num; j++) {
        process.stdout.write('#');
      }
      console.log('#');
    }
  } else {
    console.log('Missing size');
  }
}
