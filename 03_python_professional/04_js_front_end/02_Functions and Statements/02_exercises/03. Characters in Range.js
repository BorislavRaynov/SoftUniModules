function inBetween(a, b) {
  let fstNum = a.charCodeAt();
  let sndNum = b.charCodeAt();
  let start = 0;
  let end = 0;
  if (fstNum > sndNum) {
    start = sndNum;
    end = fstNum;
  } else {
    start = fstNum;
    end = sndNum;
  }
  let result = [];
  for (let i = start + 1; i < end; i++) {
    result.push(String.fromCharCode(i));
  }
  console.log(result.join(' '));
}

inBetween("a", "d");
