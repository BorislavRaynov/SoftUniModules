function attachGradientEvents() {
    const currentEl = document.getElementById('gradient')
    const result = document.getElementById('result')
    currentEl.addEventListener('mousemove', handler)

    function handler(e) {
        result.textContent = `${Math.floor((e.offsetX / 300) * 100)}%`
    }
}