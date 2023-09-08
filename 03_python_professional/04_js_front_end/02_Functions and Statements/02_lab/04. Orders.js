function totalPrice(product, quantity) {
  let result = 0;
  switch(product) {
    case "coffee":
      result = quantity * 1.5;
      break;
    case "water":
      result = quantity * 1.0;
      break;
    case "coke":
      result = quantity * 1.4;
      break;
    case "snacks":
      result = quantity * 2.0;
      break;
  }
  console.log(result.toFixed(2))
}

totalPrice("water", 5)