window.addEventListener('load', solve);

function solve() {
    const allInputEl = Array.from(document.querySelectorAll('input'))
    const addBtn = document.getElementById('add-btn')
    const allHitsContainer = document.getElementsByClassName('all-hits-container')[0]
    const totalLikes = document.querySelector('.likes p')
    const savedSongs = document.getElementsByClassName('saved-container')[0]

    addBtn.addEventListener('click', addHandler)

    function addHandler(e) {
        e.preventDefault()
        let allInputsAreFilled = allInputEl.every((input) => input.value !== '')
        if (allInputsAreFilled) {
           let [ genre, name, author, date] = allInputEl.map((el) => el.value)

            let songWrapper = createHtmlElement('div', '', allHitsContainer, '', ['hits-info'])
            createHtmlElement('img', '', songWrapper, '', '', {src: './static/img/img.png'})
            createHtmlElement('h2', `Genre: ${genre}`, songWrapper)
            createHtmlElement('h2', `Name: ${name}`, songWrapper)
            createHtmlElement('h2', `Author: ${author}`, songWrapper)
            createHtmlElement('h3', `Date: ${date}`, songWrapper)

            let saveBtn = createHtmlElement('button', 'Save song', songWrapper, '', ['save-btn'])
            let likeBtn = createHtmlElement('button', 'Like song', songWrapper, '', ['like-btn'])
            let deleteBtn = createHtmlElement('button', 'Delete', songWrapper, '', ['delete-btn'])

            likeBtn.addEventListener('click', likeHandler)
            saveBtn.addEventListener('click', saveHandler)
            deleteBtn.addEventListener('click', deleteHandler)

            allInputEl.map((el) => el.value = '')
        }
        
    }

    function likeHandler(e) {
        let currentValues = totalLikes.textContent.split(' ')
        let currentLikesStr = currentValues.pop()
        let countLikes = Number(currentLikesStr) + 1
        totalLikes.textContent = `Total Likes: ${countLikes}`
        this.disabled = 'true'
    }

    function saveHandler(e) {
        let currentSong = this.parentElement
        // this.parentElement.parentElement.removeChild(this.parentElement)
        let currentSaveBtn = currentSong.querySelector('.save-btn')
        let currentLikeBtn = currentSong.querySelector('.like-btn')
        currentSong.removeChild(currentSaveBtn)
        currentSong.removeChild(currentLikeBtn)
        savedSongs.appendChild(currentSong)
    }

    function deleteHandler(e) {
        let currentSong = this.parentElement
        currentSong.parentElement.removeChild(currentSong)
    }

    function createHtmlElement(type, content, parentNode, id, classes, attributes) {
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

}

