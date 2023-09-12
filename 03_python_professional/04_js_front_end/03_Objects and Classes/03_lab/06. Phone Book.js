function storeInfo(arr) {
  let phoneBook = {};
  for (let line of arr) {
    let info = line.split(" ");
    let names = info[0];
    let numbers = info[1];
    phoneBook[names] = numbers;
  }
  for (let data in phoneBook) {
    console.log(`${data} -> ${phoneBook[data]}`);
  }
}

storeInfo([
  "Tim 0834212554",
  "Peter 0877547887",
  "Bill 0896543112",
  "Tim 0876566344",
]);
