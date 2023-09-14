function loadRepos() {
   const currentEl = document.getElementById('res')
   fetch('https://api.github.com/users/testnakov/repos')
      .then((response) => response.text())
      .then((text) => {
         currentEl.textContent = text
      })
}