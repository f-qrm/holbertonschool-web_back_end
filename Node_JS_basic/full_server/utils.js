import fs from 'fs';

export default function readDatabase(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf-8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n').filter((line) => line.trim().length > 0);
      const students = lines.slice(1);

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

      resolve(groups);
    });
  });
}
