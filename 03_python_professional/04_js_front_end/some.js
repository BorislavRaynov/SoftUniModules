// type = string
// content = string
// id = string
// classes = Array of strings
// attributes = object

function createHtmlElement(type, content, parentNode, classes, id, attributes) {
  const htmlElement = document.createElement(type);

  if (content && type !== "input") {
    htmlElement.textContent = content;
  }

  if (content && type === "input") {
    htmlElement.value = content;
  }

  if (classes) {
    htmlElement.classList.add(...classes);
  }

  if (id) {
    htmlElement.id = id;
  }

  if (attributes) {
    for (let key in attributes) {
      htmlElement.setAttribute(key, attributes[key]);
    }
  }

  if (parentNode) {
    parentNode.appendChild(htmlElement);
  }

  return htmlElement;
}


// Object.values(inputs).every((el) => el.value !== '') проверка
// Object.values(inputs).map((el) => el.value = '') чистене
// Object.values(inputs).map((el) => el.value) мапване стойности
// Number(index) > allPeople[name].length - 1 || Number(index) < 0)

// event?.preventDefault()
