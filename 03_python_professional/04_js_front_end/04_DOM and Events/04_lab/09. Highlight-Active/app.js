function focused() {
    const elements = Array.from(document.querySelectorAll("input[type='text']"))
    for (let el of elements) {
        el.addEventListener('focus', focusHandler)
        el.addEventListener('blur', blurHandler)
    }
    
    function focusHandler(e) {
        this.parentElement.setAttribute('class', 'focused')
    }

    function blurHandler(e) {
        this.parentElement.removeAttribute('class')
    }
}
// function focused() {
//     const elements = Array.from(document.querySelectorAll("input[type='text']"))
//     for (let el of elements) {
//         el.addEventListener('click', handler)
//     }
    
//     function handler(e) {
//         this.parentElement.style.background = 'lightgrey'
//         this.parentElement.setAttribute('class', 'focused')
//         for (let el of elements) {
//             if (el !== this) {
//                 el.parentElement.removeAttribute('style')
//                 el.parentElement.removeAttribute("class")
//             }
//         }
//     }