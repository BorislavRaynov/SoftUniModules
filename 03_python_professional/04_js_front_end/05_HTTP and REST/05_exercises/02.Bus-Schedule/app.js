function solve() {
    const departBtn = document.getElementById('depart')
    const arriveBtn = document.getElementById('arrive')
    const infoEl = document.getElementsByClassName('info')[0]
    let nextStop = 'depot'
    let currentStop = ''
    const BASE_URL = 'http://localhost:3030/jsonstore/bus/schedule/'

    function depart() {
        departBtn.disabled = true
        arriveBtn.disabled = false
        fetch(`${BASE_URL}${nextStop}`)
            .then((data) => data.json())
            .then((info) => {
                infoEl.textContent = `Next stop ${info.name}`
                nextStop = info.next
                currentStop = info.name
            })
            .catch(() => {
                infoEl.textContent = 'Error'
                departBtn.disabled = true
                arriveBtn.disabled = true
            })
    }

    async function arrive() {
            departBtn.disabled = false
            arriveBtn.disabled = true
            infoEl.textContent = `Arriving at ${currentStop}`
    }

    return {
        depart,
        arrive
    };
}

let result = solve();