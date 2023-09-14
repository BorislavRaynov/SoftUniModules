function loadRepos() {
  const username = document.getElementById("username").value;
  const repos = document.getElementById("repos");

  fetch(`https://api.github.com/users/${username}/repos`)
    .then((res) => res.json())
    .then((data) => {
      repos.textContent = "";
      data
	  	.forEach((repo) => {
        const li = document.createElement("li");
        const a = document.createElement("a");
        a.href = repo.html_url;
        a.textContent = repo.full_name;
        li.appendChild(a);
        repos.appendChild(li);
      });
    })
    .catch((err) => {
      const li = document.createElement("li");
      li.textContent = err.message;
      repos.appendChild(li);
    });
}
