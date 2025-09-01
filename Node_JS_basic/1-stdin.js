process.stdin.setEncoding('utf8');

console.log('Welcome to Holberton School, what is your name?');

process.stdin.on('data', (input) => {
  console.log(`Your name is: ${input.trim()}`);
});

process.stdin.on('end', () => {
  if (!process.stdin.isTTY) {
    console.log('This important software is now closing');
  }
});
module.exports = null;
