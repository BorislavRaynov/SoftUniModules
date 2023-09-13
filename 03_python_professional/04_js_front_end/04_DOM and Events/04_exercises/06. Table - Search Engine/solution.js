function solve() {
  document.querySelector("#searchBtn").addEventListener("click", onClick);

  function onClick() {
    const allData = Array.from(document.querySelectorAll("tbody tr"));
    const searchedWordElement = document.getElementById("searchField");
    for (let el of allData) {
      if (el.classList.contains('select')) {
        el.classList.remove('select');
      }
      if (el.textContent.includes(searchedWordElement.value)) {
        el.classList.add("select");
      }
    }
    searchedWordElement.value = "";
  }
}
