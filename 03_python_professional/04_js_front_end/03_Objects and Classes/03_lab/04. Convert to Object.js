function convertToObj(strJson) {
  let currentObj = JSON.parse(strJson);
  let prop = Object.entries(currentObj);
  for (let [key, value] of prop) {
    console.log(`${key}: ${value}`);
  }
}

convertToObj('{"name": "George", "age": 40, "town": "Sofia"}');
