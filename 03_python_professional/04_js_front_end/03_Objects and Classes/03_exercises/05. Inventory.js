function register(data) {
  let listHeroes = [];
  for (let info of data) {
    let hero = { name: "", level: 0, items: "" };
    let data = info.split(" / ");
    hero.name = data[0]
    hero.level = Number(data[1])
    hero.items = data[2]
    if (!Object.values(hero).includes("")) {
      listHeroes.push(hero);
    }
  }
  listHeroes.sort((a, b) => a.level - b.level);
  for (let h of listHeroes) {
    console.log(`Hero: ${h.name}`);
    console.log(`level => ${h.level}`);
    console.log(`items => ${h.items}`);
  }
}

register([
  "Batman / 2 / Banana, Gun",
  "Superman / 18 / Sword",
  "Poppy / 28 / Sentinel, Antara",
]);
