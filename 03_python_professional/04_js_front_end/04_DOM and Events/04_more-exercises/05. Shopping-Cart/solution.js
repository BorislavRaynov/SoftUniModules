function solve() {
   const txtArea = document.getElementsByTagName('textarea')[0]
   const addBtns = Array.from(document.getElementsByClassName('add-product'))
   const checkOutBtn = document.getElementsByClassName('checkout')[0]
   const allBtns = Array.from(document.getElementsByTagName('button'))
   let allProductsAdded = {}
   checkOutBtn.addEventListener('click', checkHandler)
   for (let btn of addBtns) {
      btn.addEventListener('click', handler)
   }

   function handler(e) {
      let currentEl = this.parentElement.parentElement
      let currentPriceEl = currentEl.getElementsByClassName('product-line-price')[0]
      let currentPrice = Number(currentPriceEl.textContent)
      let currentNameEl = currentEl.getElementsByClassName('product-title')[0]
      let currentName = currentNameEl.textContent
      if (!allProductsAdded.hasOwnProperty(currentName)) {
         allProductsAdded[currentName] = 0
      }
      allProductsAdded[currentName] += currentPrice
      console.log(allProductsAdded)
      txtArea.textContent += `Added ${currentName} for ${currentPrice.toFixed(2)} to the cart.\n`
   }

   function checkHandler(e) {
      let currentOrderedProd = []
      let currentTotal = 0
      console.log(allProductsAdded)
      for (let key in allProductsAdded) {
         currentOrderedProd.push(key)
         currentTotal += allProductsAdded[key]
      }
      txtArea.textContent += `You bought ${currentOrderedProd.join(', ')} for ${currentTotal.toFixed(2)}.`
      for (let btn of allBtns) {
         btn.disabled = true
      }
   }
}