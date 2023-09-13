function calc() {
  const firstNum = document.getElementById("num1");
  const sndNum = document.getElementById("num2");
  const result = document.getElementById("sum");
  result.value = Number(firstNum.value) + Number(sndNum.value)
}
