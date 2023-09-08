function checkPalindrome(nums) {
  for (let i = 0; i < nums.length; i++) {
    let currentNumAsArr = String(nums[i]).split("");
    let loopFail = false;
    for (let idx = 0; idx < Math.ceil(currentNumAsArr.length / 2); idx++) {
      let fstNum = currentNumAsArr[idx];
      let lstNum = currentNumAsArr.reverse()[idx];
      if (fstNum === lstNum) {
        continue;
      } else {
        loopFail = true;
        break;
      }
    }
    if (loopFail) {
      console.log("false");
    } else {
      console.log("true");
    }
  }
}

// checkPalindrome([123, 323, 421, 121]);
checkPalindrome([32, 2, 232, 1010]);
