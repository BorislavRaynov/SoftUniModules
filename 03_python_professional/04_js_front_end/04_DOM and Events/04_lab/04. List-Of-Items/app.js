function addItem() {
    const currentItem = document.getElementById('newItemText')
    const item = document.getElementById('items')
    let itemToInsert = document.createElement('li')
    itemToInsert.textContent = currentItem.value
    item.appendChild(itemToInsert)
}