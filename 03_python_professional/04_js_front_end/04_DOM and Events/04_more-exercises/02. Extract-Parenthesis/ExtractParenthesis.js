function extract(content) {
  const currentTxt = document.getElementById(content).textContent;
  let result = [];
  let wordStart = 0;
  let wordEnd = 0;
  for (let i = 0; i < currentTxt.length; i++) {
    if (currentTxt.charAt(i) === "(") {
      wordStart = i + 1;
    }
    if (currentTxt.charAt(i + 1) === ")") {
      wordEnd = i;
      result.push(currentTxt.slice(wordStart, wordEnd + 1));
      wordStart = 0;
      wordEnd = 0;
    }
  }
  return result.join("; ");
}
