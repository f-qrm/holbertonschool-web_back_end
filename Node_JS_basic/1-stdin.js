process.stdin.setEncoding('utf8');

console.log('Welcome to Holberton School, what is your name?');

let inputHandled = false;

process.stdin.on('data', (input) => {
  if (!inputHandled) {
    console.log(`Your name is: ${input.trim()}`);
    inputHandled = true;
  }
});

process.stdin.on('end', () => {
  if (!process.stdin.isTTY) {
    console.log('This important software is now closing');
  }
});
