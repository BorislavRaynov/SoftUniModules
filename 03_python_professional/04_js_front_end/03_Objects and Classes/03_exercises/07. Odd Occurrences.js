function extract(text) {
  let texList = text.toLowerCase().split(" ");
  let foundWords = [];
  function findWord(name) {
    for (let w of foundWords) {
      if (w.name === name) {
        return w;
      }
    }
    return false;
  }

  for (let w of texList) {
    if (!findWord(w)) {
      let word = { name: w, times: 0 };
      foundWords.push(word);
    }
  }

  for (let w of texList) {
    let currentWord = findWord(w);
    if (currentWord) {
      currentWord.times += 1;
    }
  }
  let result = [];
  for (let w of foundWords) {
    if (w.times % 2 !== 0) {
      result.push(w.name);
    }
  }
  console.log(result.join(" "));
}

extract('Cake IS SWEET is Soft CAKE sweet Food');
