function storeAddress(input) {
  let addressBook = {};
  for (let data of input) {
    [names, address] = data.split(":");
    addressBook[names] = address;
  }

  let bookEntries = Object.entries(addressBook);
  bookEntries.sort((a, b) => a[0].localeCompare(b[0]));
  for (let info of bookEntries) {
    console.log(`${info[0]} -> ${info[1]}`)
  }
}

storeAddress([
  "Tim:Doe Crossing",
  "Bill:Nelson Place",
  "Peter:Carlyle Ave",
  "Bill:Ornery Rd",
]);
