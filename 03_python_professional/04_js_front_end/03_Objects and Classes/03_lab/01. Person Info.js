function setObject(firstName, lastName, age) {
  let person = {};
  person.firstName = firstName;
  person.lastName = lastName;
  person.age = age;
  return person;
}

console.log(setObject("Peter", "Pan", "20"));
