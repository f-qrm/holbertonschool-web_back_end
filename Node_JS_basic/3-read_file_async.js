const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf-8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n').filter((line) => line.trim().length > 0);
      const students = lines.slice(1);

      console.log(`Number of students: ${students.length}`);

      const groups = {};
      students.forEach((line) => {
        const parts = line.split(',');
        const firstname = parts[0];
        const field = parts[parts.length - 1];

        if (!groups[field]) {
          groups[field] = [];
        }
        groups[field].push(firstname);
      });

      for (const [field, list] of Object.entries(groups)) {
        console.log(`Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`);
      }

      resolve();
    });
  });
}

module.exports = countStudents;
