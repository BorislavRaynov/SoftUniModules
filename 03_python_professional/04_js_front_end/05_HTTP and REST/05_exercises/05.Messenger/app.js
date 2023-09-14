function attachEvents() {
    const submitBtn = document.getElementById('submit')
    const refreshBtn = document.getElementById('refresh')
    const inputName = document.querySelector('input[name = "author"]')
    const inputMessage = document.querySelector('input[name = "content"]')
    const textArea = document.getElementById('messages')
    const BASE_URL = 'http://localhost:3030/jsonstore/messenger'
    submitBtn.addEventListener('click', submitHandler)
    refreshBtn.addEventListener('click', refreshHandler)

    function submitHandler() {
        let author = inputName.value
        let content = inputMessage.value
        let httpHeaders = {
            method: 'POST',
            body: JSON.stringify({ author, content })
        }
        fetch(BASE_URL, httpHeaders)
            .then(() => {
                inputName.value = ''
                inputMessage.value = ''
            })
            .catch((err) => console.error(err))
    }

    async function refreshHandler() {
        textArea.disabled = 'false'
        textArea.textContent = ''
        let fullContent = []
        try {
            let data = await fetch(BASE_URL)
            let messages = await data.json()
            for (let message in messages) {
                fullContent.push(`${messages[message].author}: ${messages[message].content}`)
            }
            textArea.textContent = fullContent.join('\n')
        }

        catch(err) {
            console.error(err)
        }
    }
}

attachEvents();