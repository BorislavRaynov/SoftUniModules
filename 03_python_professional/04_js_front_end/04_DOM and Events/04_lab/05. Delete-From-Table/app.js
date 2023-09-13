function deleteByEmail() {
  const inputData = document.querySelector('input[name="email"]');
  const emailData = Array.from(document.querySelectorAll("td:nth-child(even)"));
  const result = document.getElementById("result");
  let foundEmail = emailData.find((td) => td.textContent === inputData.value);
  if (foundEmail) {
    foundEmail.parentElement.remove();
    result.textContent = "Deleted.";
  } else {
    result.textContent = 'Not found.'
  }
}
