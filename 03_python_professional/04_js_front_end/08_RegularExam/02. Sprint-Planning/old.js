window.addEventListener('load', solve);

function solve() {
    const createBtn = document.getElementById('create-task-btn')
    const mainDeleteBtn = document.getElementById('delete-task-btn')
    const section = document.getElementById('tasks-section')
    const taskId = document.getElementById('task-id')
    const totalPoints = document.getElementById('total-sprint-points')

    createBtn.addEventListener('click', createHandler)
    mainDeleteBtn.addEventListener('click', mainDelete)

    let taskIdNum = 0
    const allInputs = {
        title: document.getElementById('title'),
        textArea: document.getElementById('description'),
        selectOpt: document.getElementById('label'),
        points: document.getElementById('points'),
        assignee: document.getElementById('assignee')

    }

    let currentTaskId = null
    let currentNum = 0

    function createHandler(event) {
        event.preventDefault()
        let allAreFilled = Object.values(allInputs).every((el) => el.value !== '')
        if (allAreFilled) {
            taskIdNum += 1
            taskId.value = taskIdNum
            let [ title, textArea, selectOpt, points, assignee ] = Object.values(allInputs).map((el) => el.value)
            // currentTask = { title, textArea, selectOpt, points, assignee }
            let article = createHtmlElement('article', '', section, ['task-card'], `task-${taskIdNum}`)
            let currentIcon = null
            let currentADditionalClass = null


            if (allInputs.selectOpt.value === 'Feature') {
                currentIcon = '&#8865'
                currentADditionalClass = 'feature'
            }
            else if (allInputs.selectOpt.value === 'Low Priority Bug') {
                currentIcon = '&#9737'
                currentADditionalClass = 'low-priority'
            }
            else if(allInputs.selectOpt.value === 'High Priority Bug') {
                currentIcon = '&#9888'
                currentADditionalClass = 'high-priority'
            }

            let featureDiv = createHtmlElement('div', '', article, ['task-card-label', currentADditionalClass])
            featureDiv.innerHTML= `${selectOpt} ${currentIcon}`

            createHtmlElement('h3', title, article, ['task-card-title'])
            createHtmlElement('p', textArea, article, ['task-card-description'])
            createHtmlElement('div', `Estimated at ${points} pts`, article, ['task-card-points'])
            
            createHtmlElement('div', `Assigned to: ${assignee}`)
            let btnWrapper = createHtmlElement('div', '', article, ['task-card-action'])
            let deleteBtn = createHtmlElement('button', 'Delete', btnWrapper)

            currentNum += points
            totalPoints.textContent = `Total Points ${currentNum}pts`

            deleteBtn.addEventListener('click', deleteHandler)
            Object.values(allInputs).map((el) => el.value = '')

            function deleteHandler(e) {
                let currentEl = this.parentNode.parentNode
                taskId.value = currentEl.id
                currentTaskId = currentEl.id
                allInputs.title.value = title
                allInputs.textArea.value = textArea
                allInputs.selectOpt.value = selectOpt
                allInputs.points.value = points
                allInputs.assignee.value = assignee

                currentNum -= points
                totalPoints.textContent = `Total Points ${currentNum}pts`

                mainDeleteBtn.disabled = false
                createBtn.disabled = true


                Object.values(allInputs).map((el) => el.disabled = true)

            }
        }
    }

    function mainDelete(e) {
        let toBeDeletedEl = document.getElementById(currentTaskId)
        toBeDeletedEl.remove()

        Object.values(allInputs).map((el) => el.value = '')
        Object.values(allInputs).map((el) => el.disabled = false)

        mainDeleteBtn.disabled = true
        createBtn.disabled = false
        
    }


    function createHtmlElement(type, content, parentNode, classes, id, attributes) {
        const htmlElement = document.createElement(type);
      
        if (content && type !== "input") {
          htmlElement.textContent = content;
        }
      
        if (content && type === "input") {
          htmlElement.value = content;
        }
      
        if (classes) {
          htmlElement.classList.add(...classes);
        }
      
        if (id) {
          htmlElement.id = id;
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

}