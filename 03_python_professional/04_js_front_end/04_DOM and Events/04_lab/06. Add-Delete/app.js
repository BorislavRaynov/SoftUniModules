function addItem() {
    const currentItem = document.getElementById('newItemText')
    const item = document.getElementById('items')
    let itemToInsert = document.createElement('li')
    let linkItemToInsert = document.createElement('a')
    itemToInsert.textContent = currentItem.value
    linkItemToInsert.href = '#'
    linkItemToInsert.textContent = '[Delete]'
    linkItemToInsert.addEventListener('click', handler)
    itemToInsert.appendChild(linkItemToInsert)
    item.appendChild(itemToInsert)

    function handler(e) {
        this.parentElement.remove()
    }
}