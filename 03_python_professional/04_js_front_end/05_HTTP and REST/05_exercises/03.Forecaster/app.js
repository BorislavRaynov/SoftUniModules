function attachEvents() {
  const BASE_URL = "http://localhost:3030/jsonstore/forecaster/locations";
  const submitBtn = document.getElementById("submit");
  const inputCity = document.getElementById("location");
  const forecastContainer = document.getElementById('forecast')
  const currentWeather = document.getElementById("current")
  const threeDayWeather = document.getElementById("upcoming")
  const currentLabel = document.querySelector('#current .label')
  const upcomingLabel = document.querySelector('#upcoming .label')
  submitBtn.addEventListener("click", submitHandler);
  let searchedValue = null;
  let todayFcast = null
  let todayName = null
  let upcomingFcast = null
  let upcomingName = null

  function createHtmlElement(type, content, parentNode, id, classes, attributes) {
    const htmlElement = document.createElement(type);
  
    if (content && type !== "input") {
      htmlElement.textContent = content;
    }
  
    if (content && type === "input") {
      htmlElement.value = content;
    }
  
    if (id) {
      htmlElement.id = id;
    }
  
    if (classes) {
      htmlElement.classList.add(...classes);
    }
  
    if (attributes) {
      for (let key in attributes) {
        htmlElement.setAttribute(key, attributes[key]);
      }
    }
  
    if (parentNode) {
      parentNode.appendChild(htmlElement);
    }
  
    return htmlElement;
  }

  function insertIcon(condition, element) {
    if (condition === 'Sunny') {
        element.innerHTML = '&#x2600'
    }
    else if(condition === "Partly sunny") {
        element.innerHTML = '&#x26C5'
    }
    else if(condition === 'Overcast') {
        element.innerHTML = '&#x2601'
    }
    else if(condition === 'Rain') {
        element.innerHTML = '&#x2614'
    }

  }

  async function submitHandler() {
    currentWeather.textContent = ''
    threeDayWeather.textContent = ''
    currentWeather.appendChild(currentLabel)
    threeDayWeather.appendChild(upcomingLabel)
    forecastContainer.style.display = 'block'
    let inputValue = inputCity.value
    try {
        let data = await fetch(BASE_URL)
        let dataInfo = await data.json()
        let searchedElement = dataInfo.filter((e) => e.name === inputValue)[0]
        searchedValue = searchedElement.code
    }

    catch(err) {
        forecastContainer.textContent = 'Error'
    }

    try {
        let todayWeather = await fetch(`http://localhost:3030/jsonstore/forecaster/today/${searchedValue}`)
        let todayWeatherInfo = await todayWeather.json()
        todayFcast = todayWeatherInfo.forecast
        todayName = todayWeatherInfo.name
    }

    catch(err) {
        forecastContainer.textContent = 'Error'
    }

    try {
        let threeDayWeather = await fetch(`http://localhost:3030/jsonstore/forecaster/upcoming/${searchedValue}`)
        let threeDayWeatherInfo = await threeDayWeather.json()
        upcomingFcast = threeDayWeatherInfo.forecast
        upcomingName = threeDayWeatherInfo.name
    }

    catch(err) {
        forecastContainer.textContent = 'Error'
    }

    let mainDiv = createHtmlElement('div', '', currentWeather, '', ['forecast'])

    let currentSymbolSpan = createHtmlElement('span', '', mainDiv, '', ['condition', 'symbol'])
    let currentConditionSpan = createHtmlElement('span', '', mainDiv, '', ['condition'])
    insertIcon(todayFcast.condition, currentSymbolSpan)
    createHtmlElement('span', todayName, currentConditionSpan, '', ['forecast-data'])
    let degreeContent = `${todayFcast.low}&#176/${todayFcast.high}&#176`
    let degreeSpan = createHtmlElement('span', '', currentConditionSpan, '', ['forecast-data'] )
    degreeSpan.innerHTML = degreeContent
    createHtmlElement('span', todayFcast.condition, currentConditionSpan, '', ['forecast-data'])

    let upcomingForeCast = createHtmlElement('div', '', threeDayWeather, '', ['forecast-info'])

    for(let i=0; i < upcomingFcast.length; i++) {
      let upcomingItem = createHtmlElement('span', '', upcomingForeCast, '', ['upcoming'])
      let symbolUpcoming = createHtmlElement('span', '',upcomingItem, '', ['symbol'])
      insertIcon(upcomingFcast[i].condition, symbolUpcoming)
      let upcomingDegreeData = `${upcomingFcast[i].low}&#176/${upcomingFcast[i].high}&#176`
      let upcomingDegreeSpan = createHtmlElement('span', '', upcomingItem, '', ['forecast-data'])
      upcomingDegreeSpan.innerHTML = upcomingDegreeData
      createHtmlElement('span', upcomingFcast[i].condition, upcomingItem, '', ['forecast-data'])
    }
  }
}
attachEvents()
