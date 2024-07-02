import { useState } from "react"
import KillCounter from "./KillCounter"
import './Counter.css'

export default function Counter() {
    const [count, setCount] = useState(0)

    const incrementBtnClickHandler = () => {
        setCount(count + 1);
    }

    function resetBtnClickHandler() {
        return setCount(0)
    }

    const decrementBtnClickHandler = () => {
        setCount(count - 1)
    }

    let countText = `Positive ${count}`
    let color = 'green'
    if (count < 0) {
        countText = `Negative ${count}`
        color = 'red'
    }

    return (
        <>
            <h2>Counter</h2>

            <KillCounter count={count}/>

            <p
                style={{color}} 
                className={count > 0 ? 'positive-text' : 'negative-text'}
            >
                {countText}
            </p>

            <button onClick={decrementBtnClickHandler}>-</button>
            <button onClick={resetBtnClickHandler}>Reset</button>
            <button onClick={incrementBtnClickHandler}>+</button>
        </>

    )
}