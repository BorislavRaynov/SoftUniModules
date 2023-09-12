function employee(data) {
  let employees = data.reduce((info, empl) => {
    info[empl] = empl.length
    return info
  }, {})
  for (let e in employees) {
    console.log(`Name: ${e} -- Personal Number: ${employees[e]}`)
  }
}

employee([
  "Silas Butler",
  "Adnaan Buckley",
  "Juan Peterson",
  "Brendan Villarreal",
]);
