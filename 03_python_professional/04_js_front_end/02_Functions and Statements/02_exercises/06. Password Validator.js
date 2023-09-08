// function passwordValidator(text) {
//   function checkLength() {
//     return (text >= 6 && text <= 10);
//   }

//   function checkValidSymbols() {
//     return /[^A-z|^0-9]/.test(text);
//   }

//   function countDigit() {
//     let countNumbers = 0;
//     for (let i = 0; i < text.length; i++) {
//       if (text.charAt(i) >= 0) {
//         countNumbers += 1;
//       }
//     }
//     if (countNumbers < 2) {
//       return false;
//     } else {
//       return true;
//     }
//   }

//   if (!checkLength()) {
//     console.log("Password must be between 6 and 10 characters");
//   }

//   if (!checkValidSymbols()) {
//     console.log("Password must consist only of letters and digits");
//   }

//   if (!countDigit()) {
//     console.log("Password must have at least 2 digits");
//   }

//   if (checkLength() && checkValidSymbols() && countDigit()) {
//     console.log("Password is valid");
//   }
// }

function passwordValidator(text) {
  let notCorrectLength = false;
  let notOnlyLetAndNum = false;
  let hasNotTwoNum = false;
  let countNumbers = 0

  if (text.length < 6 || text.length > 10) {
    notCorrectLength = true;
  }
  if (/[^A-z|^0-9]/.test(text)) {
    notOnlyLetAndNum = true;
  }

  for (let i = 0; i < text.length; i++) {
    if (text.charAt(i) >= 0) {
      countNumbers += 1;
    }
  }

  if (countNumbers < 2) {
    hasNotTwoNum = true;
  }

  if (notCorrectLength) {
    console.log("Password must be between 6 and 10 characters");
  }
  if (notOnlyLetAndNum) {
    console.log("Password must consist only of letters and digits");
  }
  if (hasNotTwoNum) {
    console.log("Password must have at least 2 digits");
  }
  if (
    notCorrectLength === false &&
    notOnlyLetAndNum === false &&
    hasNotTwoNum === false
  ) {
    console.log("Password is valid");
  }
}

passwordValidator('Pa$s$s');
