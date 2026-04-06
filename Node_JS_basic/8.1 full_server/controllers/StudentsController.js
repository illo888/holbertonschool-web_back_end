import readDatabase from '../utils';

export default class StudentsController {
  static getAllStudents(req, res) {
    const database = process.argv[2];

    readDatabase(database)
      .then((fields) => {
        let output = 'This is the list of our students';

        const sortedFields = Object.keys(fields).sort((a, b) =>
          a.toLowerCase().localeCompare(b.toLowerCase())
        );

        sortedFields.forEach((field) => {
          const list = fields[field];
          output += `\nNumber of students in ${field}: ${list.length}. List: ${list.join(', ')}`;
        });

        res.status(200).send(output);
      })
      .catch(() => {
        res.status(500).send('Cannot load the database');
      });
  }

  static getAllStudentsByMajor(req, res) {
    const database = process.argv[2];
    const { major } = req.params;

    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    readDatabase(database)
      .then((fields) => {
        const list = fields[major] || [];
        res.status(200).send(`List: ${list.join(', ')}`);
      })
      .catch(() => {
        res.status(500).send('Cannot load the database');
      });
  }
}
