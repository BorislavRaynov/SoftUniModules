function create(words) {
   const mainContent = document.getElementById('content')
   for (let el of words) {
      let currentElement = document.createElement('div')
      let currentParagraph = document.createElement('p')
      currentParagraph.textContent = el
      currentParagraph.style.display = 'none'
      currentElement.addEventListener('click', handler)
      currentElement.appendChild(currentParagraph)
      mainContent.appendChild(currentElement)
   }

   function handler(e) {
      this.children[0].style.display = 'block'
   }
}