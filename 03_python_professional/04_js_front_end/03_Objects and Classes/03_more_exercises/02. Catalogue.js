function catalogue(data) {
  let storage = data.sort(
    (a, b) => a.toLowerCase().localeCompare(b.toLowerCase())
  ) 
  let storageGrouped = {};
  for (let info of storage) {
    let infoSplitted = info.split(" : ");
    let name = infoSplitted[0];
    let price = infoSplitted[1];
    let group = name[0];
    let productObj = { name, price };
    if (!Object.keys(storageGrouped).includes(group)) {
      storageGrouped[group] = [];
    }
    storageGrouped[group].push(productObj);
  }

  let storageEntries = Object.entries(storageGrouped);
  for (let [group, items] of storageEntries) {
    console.log(group);
    for (let el of items) {
      console.log(`  ${el.name}: ${el.price}`);
    }
  }
}

catalogue([
  "Appricot : 20.4",
  "Fridge : 1500",
  "TV : 1499",
  "Deodorant : 10",
  "Boiler : 300",
  "Apple : 1.25",
  "Anti-Bug Spray : 15",
  "T-Shirt : 10",
]);
