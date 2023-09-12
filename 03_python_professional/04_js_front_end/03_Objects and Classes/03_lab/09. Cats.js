function creatingCats(input) {
  class Cat {
    constructor(name, age) {
      this.name = name;
      this.age = age;
    }
    meow() {
      console.log(`${this.name}, age ${this.age} says Meow`);
    }
  }
  let cats = [];
  for (let data of input) {
    [catName, catAge] = data.split(" ");
    cats.push(new Cat(catName, catAge));
  }
  for (let cat of cats) {
    cat.meow();
  }
}

creatingCats(["Candy 1", "Poppy 3", "Nyx 2"]);
