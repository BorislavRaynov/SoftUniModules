function sum(num) {
  let nums = String(num).split("");
  let evenSum = 0;
  let oddSum = 0;
  for (let i = 0; i < nums.length; i++) {
    let currentNum = Number(nums[i]);
    if (currentNum % 2 === 0) {
      evenSum += currentNum;
    } else {
      oddSum += currentNum;
    }
  }
  let result = `Odd sum = ${oddSum}, Even sum = ${evenSum}`
  console.log(result)
}

sum(3495892137259234);
