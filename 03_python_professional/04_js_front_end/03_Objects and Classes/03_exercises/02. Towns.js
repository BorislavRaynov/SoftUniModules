function towns(data) {
  let cities = []
  for (let info of data) {
    let [ town, latitude, longitude ] = info.split(' | ')
    cities.push({town, latitude: Number(latitude).toFixed(2), longitude: Number(longitude).toFixed(2)})
   }

   cities.forEach(town => console.log(town))
}

towns(["Sofia | 42.696552 | 23.32601", "Beijing | 39.913818 | 116.363625"]);
