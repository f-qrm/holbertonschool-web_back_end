process.stdin.setEncoding('utf8');

console.log('Welcome to Holberton School, what is your name?')
process.stdin.on('data', function(input) {
  console.log('Your name is: ' + input.trim());
});
process.stdin.on('end', function() {
  console.log('This important software is now closing')
});
