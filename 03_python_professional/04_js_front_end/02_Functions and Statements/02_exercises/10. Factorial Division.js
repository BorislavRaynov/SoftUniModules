function factorialDivision(numOne, numTwo) {
  let fstRes = 1;
  let sndRes = 1;
  for (let i = numOne; i > 0; i--) {
    fstRes *= i;
  }
  for (let n = numTwo; n > 0; n--) {
    sndRes *= n;
  }
  let result = fstRes / sndRes;
  console.log(result.toFixed(2));
}

factorialDivision(6, 2);