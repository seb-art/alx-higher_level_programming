#!/usr/bin/node

// A sript that prints argument

console.log(typeof process.argv[2] === 'undefined' ? 'No argument' : process.argv[2]);
