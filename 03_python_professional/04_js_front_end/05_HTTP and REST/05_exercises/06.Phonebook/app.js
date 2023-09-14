function attachEvents() {
  const loadBtn = document.getElementById("btnLoad");
  const createBtn = document.getElementById("btnCreate");
  const contactList = document.getElementById("phonebook");
  const inputName = document.getElementById("person");
  const inputNumber = document.getElementById("phone");
  const BASE_URL = "http://localhost:3030/jsonstore/phonebook";
  loadBtn.addEventListener("click", loadHandler);
  createBtn.addEventListener("click", createHandler);

  async function loadHandler() {
    try {
      let response = await fetch(BASE_URL);
      let data = await response.json();
      data = Object.values(data);
      for (let contact of data) {
        let li = document.createElement("li");
        let deleteBtn = document.createElement("button");
        deleteBtn.id = contact._id;
        deleteBtn.textContent = "Delete";
        deleteBtn.addEventListener("click", deleteHandler);
        li.textContent = `${contact.person}: ${contact.phone}`;
        li.appendChild(deleteBtn);
        contactList.appendChild(li);
      }
    } catch (err) {
      console.error(err);
    }
  }

  function createHandler() {
    let person = inputName.value;
    let phone = inputNumber.value;
    httpHeaders = {
      method: "POST",
      body: JSON.stringify({ person, phone }),
    };

    fetch(BASE_URL, httpHeaders)
      .then(() => {
        contactList.innerHTML = "";
      })
      .then(loadHandler)
      .then(() => {
        inputName.value = "";
        inputNumber.value = "";
      })
      .catch((err) => {
        console.error(err);
      });
  }

  function deleteHandler(e) {
    let httpHeaders = {
      method: "DELETE",
    };
    fetch(`${BASE_URL}/${this.id}`, httpHeaders)
      .then(() => {
        contactList.innerHTML = "";
      })
      .then(loadHandler)
      .catch((err) => {
        console.error(err);
      });
  }
}

attachEvents();
