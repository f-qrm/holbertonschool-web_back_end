import readDatabase from '../utils';

export default class StudentsController {
  static async getAllStudents(req, res) {
    res.type('text');
    const pathData = process.argv[2];
    try {
      const data = await readDatabase(pathData);
      let output = ('This is the list of our students\n');
      const fields = Object.keys(data);

      fields.sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()));

      for (const field of fields) {
        const list = data[field];
        const count = list.length;
        const line = `Number of students in ${field}: ${count}. List: ${list.join(', ')}`;
        output += `${line}\n`;
      }

      res.status(200).send(output);
    } catch (err) {
      res.status(500).send('Cannot load the database');
    }
  }

  static async getAllStudentsByMajor(req, res) {
    res.type('text');
    const pathData = process.argv[2];
    const { major } = req.params;

    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).send('Major parameter must be CS or SWE');
      return;
    }
    try {
      const data = await readDatabase(pathData);
      const list = data[major];
      res.status(200).send(`List: ${list.join(', ')}`);
    } catch (err) {
      res.status(500).send('Cannot load the database');
    }
  }
}
