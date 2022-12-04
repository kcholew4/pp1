const fs = require("fs");

const f = (age, course, average) => {
  file = fs.readFileSync("test.json");
  data = JSON.parse(file);

  const filtered = data.filter((student) => {
    if (student.age < age) {
      return false;
    }

    const desiredCourse = student.studies.courses.find((single) => single.name === course);

    if (!desiredCourse) {
      return false;
    }

    const mean = desiredCourse.grades.reduce((a, v) => a + v) / desiredCourse.grades.length;

    if (mean < average) {
      return false;
    }

    return true;
  });

  return filtered.length;
};

const students = f(21, "statistics", 4);

console.log(students);
