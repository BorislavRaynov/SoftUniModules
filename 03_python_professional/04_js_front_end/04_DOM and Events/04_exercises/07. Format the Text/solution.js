function solve() {
  const targetElement = document.getElementById("output");
  const textElement = document.getElementById("input");
  let arrOfInputText = textElement.value.split(".");
  arrOfInputText.pop();
  while (arrOfInputText.length > 0) {
    let newParagraph = document.createElement(`p`);
    let currentText = arrOfInputText.splice(0, 3).map((p) => p.trimStart());
    newParagraph.textContent = currentText.join(".") + ".";
    targetElement.appendChild(newParagraph);
  }
}
