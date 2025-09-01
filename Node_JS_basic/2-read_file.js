const fs = require('fs');

function countStudents(path) {
  try {
    const content = fs.readFileSync(path, 'utf-8');

    const lines = content.split('\n');
    const newLines = lines.slice(1);
    const filtredLines = newLines.filter((line) => line.trim().length > 0);
    const numberOfStudents = filtredLines.length;
    console.log(`Number of students: ${numberOfStudents}`);

    const fields = {};
    for (const line of filtredLines) {
      const parts = line.split(',');
      const firstname = parts[0];
      const field = parts[parts.length - 1];

      if (!fields[field]) {
        fields[field] = [];
      }
      fields[field].push(firstname);
    }
    for (const [field, students] of Object.entries(fields)) {
      console.log(`Number of students in ${field}: ${students.length}. List: ${students.join(', ')}`);
    }
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}
module.exports = countStudents;
