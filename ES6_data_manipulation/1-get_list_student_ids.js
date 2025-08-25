export default function getListStudentIds(arr) {
  if (!Array.isArray(arr))
    return [];
  const newArr = arr.map((element) => {
    return element.id;
  });
  return newArr
}
