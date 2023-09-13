function solve() {
  const [inputText, infoText] = document.getElementsByTagName("textarea");
  const [generateBtn, buyBtn] = document.getElementsByTagName("button");
  const tBody = document.getElementsByTagName("tbody")[0];
  generateBtn.addEventListener("click", generateHandler);
  buyBtn.addEventListener("click", buyHandler);

  function generateHandler(e) {
    const itemParent = document.getElementsByTagName("tbody")[0];
    let items = JSON.parse(inputText.value);
    for (let { img, name, price, decFactor } of items) {
      let tableRow = createHtmlElement("tr", "", tBody);
      let fstColumnTd = createHtmlElement('td', '', tableRow);
      createHtmlElement('img', '', fstColumnTd, '', '', {src: img})
      let sndColumTd = createHtmlElement('td', '', tableRow)
      createHtmlElement('p', name, sndColumTd)
      let trdColumTd = createHtmlElement('td', '', tableRow)
      createHtmlElement('p', price, trdColumTd)
      let forthColumTd = createHtmlElement('td', '', tableRow)
      createHtmlElement('p', decFactor, forthColumTd)
      let fthColumTd = createHtmlElement('td', '', tableRow)
      createHtmlElement('input', '', fthColumTd, '', '', {type: 'checkbox'})
    }
  }

  function buyHandler(e) {
    const allEnabled = Array.from(tBody.querySelectorAll('input:checked'))
    let boughtItems = []
    let totalPrice = 0
    let totalDecFac = 0
    for (let buyItem of allEnabled) {
      let currentItem = buyItem.parentElement.parentElement
      boughtItems.push(currentItem.getElementsByTagName('td')[1].textContent)
      totalPrice += Number(currentItem.getElementsByTagName('td')[2].textContent)
      totalDecFac += Number(currentItem.getElementsByTagName('td')[3].textContent)
    }
    let result = []
    result.push(`Bought furniture: ${boughtItems.join(', ')}`)
    result.push(`Total price: ${totalPrice.toFixed(2)}`)
    result.push(`Average decoration factor: ${totalDecFac / boughtItems.length}`)
    infoText.value = result.join('\n')
  }

  function createHtmlElement(
    type,
    content,
    parentNode,
    id,
    classes,
    attributes
  ) {
    const htmlElement = document.createElement(type);

    if (content && type !== "input") {
      htmlElement.textContent = content;
    }

    if (content && type === "input") {
      htmlElement.value = content;
    }

    if (id) {
      htmlElement.id = id;
    }

    if (classes) {
      htmlElement.classList.add(...classes);
    }

    if (parentNode) {
      parentNode.appendChild(htmlElement);
    }

    if (attributes) {
      for (let key in attributes) {
        htmlElement.setAttribute(key, attributes[key]);
      }
    }

    return htmlElement;
  }
}
