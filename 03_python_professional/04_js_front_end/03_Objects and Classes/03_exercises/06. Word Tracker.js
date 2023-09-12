function findWords(data) {
  let foundWords = [];
  let searchesWords = data[0].split(" ");
  let wordsList = data.slice(1);
  for (let w of searchesWords) {
    let word = { name: "", times: 0 };
    word.name = w;
    foundWords.push(word);
  }

  for (let el of wordsList) {
    for (let w of foundWords) {
      if (w.name === el) {
        w.times += 1;
      }
    }
  }

  foundWords.sort((a, b) => b.times - a.times);
  for (let w of foundWords){
    console.log(`${w.name} - ${w.times}`)
  }
}

findWords([
    'is the', 
    'first', 'sentence', 'Here', 'is', 'another', 'the', 'And', 'finally', 'the', 'the', 'sentence']
    );
