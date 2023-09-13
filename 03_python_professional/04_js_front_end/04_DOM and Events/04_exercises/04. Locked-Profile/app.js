function lockedProfile() {
  const allBtnS = document.getElementsByTagName("button");
  for (let btn of allBtnS) {
    btn.addEventListener("click", btnHandler);
  }

  function btnHandler(e) {
    let currentBtnText = this.textContent;
    let elementToShow = this.parentElement.getElementsByTagName("div")[0];
    if (checkProfileState(this) === "unlock") {
      if (currentBtnText === "Show more") {
        elementToShow.style.display = "block";
        this.textContent = "Hide it";
      } else {
        elementToShow.style.display = "none";
        this.textContent = "Show more";
      }
    }
  }

  function checkProfileState(el) {
    let profileRadios = Array.from(
      el.parentElement.querySelectorAll("input[type='radio']")
    );
    for (let radio of profileRadios) {
      if (radio.checked) {
        return radio.value;
      }
    }
  }
}
