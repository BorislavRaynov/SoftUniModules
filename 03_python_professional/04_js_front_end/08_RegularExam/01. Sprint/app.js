function solve(data) {
    let num = data.shift()
    let initial = data.splice(0, num)
    let allPeople = {}
    for (let data of initial ) {
        let [ name, taskId, title, status, estimatedPoints ] = data.split(':')
        if (!allPeople.hasOwnProperty(name)) {
            allPeople[name] = []
        }
        allPeople[name].push({taskId, title, status, estimatedPoints})
    }

    for (let info of data) {
        
        if (info.includes('Add New')) {
            let [ _command, name, taskId, title, status, estimatedPoints ] = info.split(':')
            if (allPeople.hasOwnProperty(name)) {
                allPeople[name].push({ taskId, title, status, estimatedPoints })
            }
            else {
                console.log(`Assignee ${name} does not exist on the board!`)
            }
        }

        else if(info.includes('Change Status')) {
            let [ _command, name, searchedTaskId, newStatus ] = info.split(':')
            if (!allPeople.hasOwnProperty(name)) {
                console.log(`Assignee ${name} does not exist on the board!`)
            }
            else {
                let taskIdNotExist = true
                for (let task of allPeople[name]) {
                    if (task.taskId === searchedTaskId) {
                        task.status = newStatus
                        taskIdNotExist = false
                    }
                }
                if (taskIdNotExist) {
                    console.log(`Task with ID ${searchedTaskId} does not exist for ${name}!`)
                }
            }
        }
        else if(info.includes('Remove Task')) {
            let [ _command, name, index] = info.split(':')
            if (!allPeople.hasOwnProperty(name)) {
                console.log(`Assignee ${name} does not exist on the board!`)
            }
            else if (Number(index) > allPeople[name].length - 1 || Number(index) < 0) {
                console.log('Index is out of range!')
            }
            else {
                allPeople[name].splice(Number(index), 1)
            }
        }
    }

    let todoPoints = 0
    let inProgressPoints = 0
    let codeReviewPoints = 0
    let donePoints = 0
    
    for (let key in allPeople) {
        let currentData = allPeople[key]
        for (let infoData of currentData) {
            if (infoData.status === 'ToDo') {
                todoPoints += Number(infoData.estimatedPoints)
            }
            else if(infoData.status === 'In Progress') {
                inProgressPoints += Number(infoData.estimatedPoints)
            }
            else if(infoData.status === 'Code Review') {
                codeReviewPoints += Number(infoData.estimatedPoints)
            }
            else if(infoData.status === 'Done') {
                donePoints += Number(infoData.estimatedPoints)
            }
        }
    }
    console.log(`ToDo: ${todoPoints}pts`)
    console.log(`In Progress: ${inProgressPoints}pts`)
    console.log(`Code Review: ${codeReviewPoints}pts`)
    console.log(`Done Points: ${donePoints}pts`)

    if (donePoints >= inProgressPoints + codeReviewPoints + todoPoints) {
        console.log('Sprint was successful!')
    }
    else {
        console.log('Sprint was unsuccessful...')
    }
}

solve(  [
    '4',
    'Kiril:BOP-1213:Fix Typo:Done:1',
    'Peter:BOP-1214:New Products Page:In Progress:2',
    'Mariya:BOP-1215:Setup Routing:ToDo:8',
    'Georgi:BOP-1216:Add Business Card:Code Review:3',
    'Add New:Sam:BOP-1237:Testing Home Page:Done:3',
    'Change Status:Georgi:BOP-1216:Done',
    'Change Status:Will:BOP-1212:In Progress',
    'Remove Task:Georgi:3',
    'Change Status:Mariya:BOP-1215:Done',
]
)