function printObject(obj) {
  let city = Object.entries(obj);
  for (let [key, value] of city) {
    console.log(`${key} -> ${value}`)
  }

}

printObject({
  name: "Sofia",
  area: 492,
  population: 1238438,
  country: "Bulgaria",
  postCode: "1000",
});
