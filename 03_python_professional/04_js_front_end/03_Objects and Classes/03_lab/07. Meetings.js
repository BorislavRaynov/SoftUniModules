function meetingManager(input) {
    let meetings = {};
    for (let line of input) {
        let [weekday, names] = line.split(' ');
        if (meetings.hasOwnProperty(weekday)) {
            console.log(`Conflict on ${weekday}!`)
        } else {
            meetings[weekday] = names
            console.log(`Scheduled for ${weekday}`)
        }
    }

    for (let data in meetings) {
        console.log(`${data} -> ${meetings[data]}`)
    }
}

meetingManager([
  "Friday Bob",
  "Saturday Ted",
  "Monday Bill",
  "Monday John",
  "Wednesday George",
]);
