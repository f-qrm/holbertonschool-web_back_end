export default function createEmployeesObject(departmentName, employees) {
  const newC = { [departmentName]: employees };
  return newC;
}
