function airPort(data) {
    let flights = data[0]
    let changedFlights = data[1]
    let command = data[2][0]
    let currentFlights = []
    for (let plane of flights) {
        let info = plane.split(' ')
        let number = info[0]
        let destination = info[1]
        let status = 'Ready to fly'
        currentFlights.push({number, destination, status})
    }

    for (let plane of changedFlights) {
        let currentInfo = plane.split(' ')
        let num = currentInfo[0]
        let newStatus = currentInfo[1]
        let currentPlane = findFlight(num)
        if (currentPlane) {
            currentPlane.status = newStatus
        }
    }

    function findFlight(num) {
        for (let fl of currentFlights) {
            if (Object.values(fl).includes(num)){
                return fl
            } 
        }
    }

    function filteredByStatus(command) {
        let res = []
        for (let flight of currentFlights) {
            if (Object.values(flight).includes(command)) {
                res.push(flight)
            }
        }
        return res
    }

    let finalResult = filteredByStatus(command)

    for (let el of finalResult) {
        console.log(`{ Destination: '${el.destination}', Status: '${el.status}' }`)
    }
}

airPort([
  [
    "WN269 Delaware",
    "FL2269 Oregon",
    "WN498 Las Vegas",
    "WN3145 Ohio",
    "WN612 Alabama",
    "WN4010 New York",
    "WN1173 California",
    "DL2120 Texas",
    "KL5744 Illinois",
    "WN678 Pennsylvania",
  ],
  [
    "DL2120 Cancelled",
    "WN612 Cancelled",
    "WN1173 Cancelled",
    "SK430 Cancelled",
  ],
  ["Cancelled"],
]);
