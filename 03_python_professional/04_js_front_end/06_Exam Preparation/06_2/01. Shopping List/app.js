function solve([products, ...commands]) {
  let productsAsArr = products.split("!");

  for (let command of commands) {
    let arrOfCommand = command.split(" ");

    if (arrOfCommand.includes("Correct")) {
      let newItem = arrOfCommand.pop();
      let oldItem = arrOfCommand.pop();
      if (productsAsArr.includes(oldItem)) {
        let index = productsAsArr.indexOf(oldItem);
        productsAsArr[index] = newItem;
      }
    } else {
      let currentCommand = arrOfCommand[0];
      let item = arrOfCommand[1];

      if (currentCommand === "Urgent") {
        if (!productsAsArr.includes(item)) {
          productsAsArr.unshift(item);
        }
      } else if (currentCommand === "Unnecessary") {
        if (productsAsArr.includes(item)) {
          let index = productsAsArr.indexOf(item);
          productsAsArr.splice(index, 1);
        }
      } else if (currentCommand === "Rearrange") {
        if (productsAsArr.includes(item)) {
          let index = productsAsArr.indexOf(item);
          productsAsArr.push(productsAsArr.splice(index, 1));
        }
      }
    }
  }
  console.log(productsAsArr.join(", "));
}

solve([
  "Tomatoes!Potatoes!Bread",
  "Unnecessary Milk",
  "Urgent Tomatoes",
  "Go Shopping!",
]);
