function editElement(element, searchedTxt, newTxt) {
    element.textContent = element.textContent.split(searchedTxt).join(newTxt)
    
}