export default function getStudentIdsSum(arr) {
  if (!Array.isArray(arr))
    return [];
  const initialValue = 0;
  const newArray = arr.reduce((accumulator, currentValue) =>
    accumulator + currentValue.id, initialValue);
  return newArray
}
