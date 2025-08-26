export default function cleanSet(set, startString) {
  if (startString === '' || startString == null || startString == undefined) return '';
  const newList = []
  for (const value of set) {
    if (value.startsWith(startString)) {
      newList.push(value.slice(startString.length))
    }
  }
  return newList.join('-')
}
