function loading(num) {
  let symbolOne = '%'
  let symbolTwo = '.'
  let fstHalf = symbolOne.repeat(num / 10)
  let sndHalf = symbolTwo.repeat(10 - fstHalf.length)
  let result = fstHalf + sndHalf

  if (result.includes(".")) {
    console.log(`${num}% [${result}]`);
    console.log("Still loading...");
  } else {
    console.log("100% Complete!");
    console.log(`[${result}]`);
  }
}

loading(100);
