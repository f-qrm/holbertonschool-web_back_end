export default function getStudentsByLocation(arr, city) {
  if (!Array.isArray(arr))
    return [];
  const newArray = arr.filter(arr => arr.location === city)
  return newArray
}
