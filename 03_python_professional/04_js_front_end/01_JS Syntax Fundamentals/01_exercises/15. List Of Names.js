function solve(names) {
  let namesSorted = names.sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()));
  for (let i=1; i <= namesSorted.length; i++)
    console.log(`${i}.${namesSorted[i-1]}`)
}

solve(["John", "Bob", "Christina", "Ema"])
