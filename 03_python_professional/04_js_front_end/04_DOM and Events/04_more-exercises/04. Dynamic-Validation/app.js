function validate() {
  const inputArea = document.getElementById("email");
  inputArea.addEventListener("change", handler);

  function handler() {
    let email = inputArea.value;
    inputArea.classList.remove("error")
    if (/^[a-z]+@[a-z]+\.[a-z]+/.test(email) === false) {
      inputArea.classList.add("error");
    }
  }
}
