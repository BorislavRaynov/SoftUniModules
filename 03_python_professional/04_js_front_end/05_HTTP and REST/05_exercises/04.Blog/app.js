function attachEvents() {
    const loadingBtn = document.getElementById('btnLoadPosts')
    const viewBtn = document.getElementById('btnViewPost')
    const selectArea = document.getElementById('posts')
    loadingBtn.addEventListener('click', loadingHandler)
    viewBtn.addEventListener('click', viewHandler)
    const postH1 = document.getElementById('post-title')
    const postBody = document.getElementById('post-body')
    const commentsUlEl= document.getElementById('post-comments')
    let allPosts = null

    async function loadingHandler() {
        try {
            let loadResponse = await fetch('http://localhost:3030/jsonstore/blog/posts')
            let posts = await loadResponse.json()
            allPosts = posts
            for (let post in posts) {
                let postElement = document.createElement('option')
                postElement.value = post
                postElement.textContent = posts[post].title
                selectArea.appendChild(postElement)
            }
        }
        
        catch(err) {
            console.error(err)
        }
    }

    async function viewHandler() {
        let allOptions = Array.from(selectArea.children)
        let currentOption = allOptions.filter((op) => op.selected)[0]
        let currentPostId = currentOption.value 
        postH1.textContent = allPosts[currentPostId].title
        postBody.textContent = allPosts[currentPostId].body
        try {
            let viewResponse = await fetch('http://localhost:3030/jsonstore/blog/comments')
            let comments = await viewResponse.json()
            let allCurrentComments = []
            for (let com in comments) {
                if (comments[com].postId === currentPostId) {
                    allCurrentComments.push(comments[com].text)
                } 
            }
            commentsUlEl.textContent = ''
            for (let comTxt of allCurrentComments) {
                let li = document.createElement('li')
                li.textContent = comTxt
                commentsUlEl.appendChild(li)
            }
        }

        catch(err) {
            console.error(err)
        }
    }
}

attachEvents();