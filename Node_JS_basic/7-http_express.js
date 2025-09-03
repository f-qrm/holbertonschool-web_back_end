const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();

app.get('/', (req, res) => {
  res.set('Content-Type', 'text/plain');
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  res.set('Content-Type', 'text/plain');

  let output = '';
  const database = process.argv[2];
  const originalLog = console.log;

  console.log = (msg) => { output += `${msg}\n`; };
  try {
    await countStudents(database);
    output = output.trimEnd();
    res.send(`This is the list of our students\n${output}`);
  } catch (err) {
    console.log = originalLog;
    res.end('Cannot load the database');
    return;
  } finally {
  console.log = originalLog;
  }
});

app.listen(1245);
module.exports = app;
