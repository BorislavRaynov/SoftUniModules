function check(numOne, numTwo, numThree) {
  let counter = 0;
  if (numOne < 1) {
    counter += 1;
  }

  if (numTwo < 1) {
    counter += 1;
  }

  if (numThree < 1) {
    counter += 1;
  }

  if (counter % 2 === 1) {
    console.log("Positive");
  } else {
    console.log("Negative");
  }
}

check(-6,
    -12,
     0
    )