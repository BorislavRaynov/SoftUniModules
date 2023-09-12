function localeStore(currentProducts, orderedProducts) {

  let listProducts = [...currentProducts, ...orderedProducts];
  let store = {}
  for (let i = 0; i < listProducts.length; i+=2) {
    [product, quantity] = [listProducts[i], Number(listProducts[i + 1])];
    if (!store.hasOwnProperty(product)){
      store[product] = quantity
    } else {
      store[product] += quantity
    }
  }

  for (let p in store) {
    console.log(`${p} -> ${store[p]}`);
  }
}

localeStore(
  ["Chips", "5", "CocaCola", "9", "Bananas", "14", "Pasta", "4", "Beer", "2"],
  ["Flour", "44", "Oil", "12", "Pasta", "7", "Tomatoes", "70", "Bananas", "30"]
);
