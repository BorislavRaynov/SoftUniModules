// АСИНХРОННИ ОПЕРАЦИИ .THEN/.CATCH БЛОКОВЕ

// function loadCommits() {
//     const username = document.getElementById('username')
//     const repository = document.getElementById('repo')
//     const commits = document.getElementById('commits')
//     const loader = document.getElementById('loader')

//     loader.display = 'block'
//     fetch(`https://api.github.com/repos/${username.value}/${repository.value}/commits`)
//         .then((res) => res.json())
//         .then((data) => {
//             loader.style.display = 'none'
//             data
//                 .forEach(({ commit }) => {
//                     const li = document.createElement('li')
//                     li.textContent = `${commit.author.name}: ${commit.message}`
//                     commits.appendChild(li)
//             });
//         })
//         .catch((err) => {
//             const li = document.createElement('li')
//             li.textContent = err.message
//             commits.appendChild(li)
//         })
// }

// АСИНХРОННА ФУНКЦИЯ ASYNC/AWAIT (.TRY/.CATCH) 

async function loadCommits() {
    const username = document.getElementById('username')
    const repository = document.getElementById('repo')
    const commits = document.getElementById('commits')
    const loader = document.getElementById('loader')

    try {
        loader.display = 'block'
        let commitsRes = await fetch(`https://api.github.com/repos/${username.value}/${repository.value}/commits`)
        let data = await commitsRes.json()
        loader.style.display = 'none'
        data
            .forEach(({ commit }) => {
                const li = document.createElement('li')
                li.textContent = `${commit.author.name}: ${commit.message}`
                commits.appendChild(li)
        });
    }

    catch(err) {
        const li = document.createElement('li')
        li.textContent = err.message
        commits.appendChild(li)
    }
}