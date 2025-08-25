export default function updateStudentGradeByCity(arr, city, newGrades) {
  if (!Array.isArray(arr))
    return [];
  return arr.filter(arr => arr.location === city).map(student => {
   const obj = newGrades.find(nG => nG.studentId == student.id)
   return {
    ...student,
    grade: obj ? obj.grade:("N/A")
   }
  });
}
