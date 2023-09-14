function getInfo() {
    const inputId = document.getElementById('stopId')
    const BASE_URL = 'http://localhost:3030/jsonstore/bus/businfo/'
    let busStopID = inputId.value
    const stopName = document.getElementById('stopName')
    const busesCurrent = document.getElementById('buses')

    fetch(`${BASE_URL}${busStopID}`)
        .then((info) => info.json())
        .then((data) => {
            busesCurrent.textContent = ''
            stopName.textContent = data.name
            for (let bus in data.buses) {
                let li = document.createElement('li')
                let result = `Bus ${bus} arrives in ${data.buses[bus]} minutes`
                li.textContent = result
                busesCurrent.appendChild(li)
            }
        })
        .catch((err) => {
            stopName.textContent = 'Error'
        })
}