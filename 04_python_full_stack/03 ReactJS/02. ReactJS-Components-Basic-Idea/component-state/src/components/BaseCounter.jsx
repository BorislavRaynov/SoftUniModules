import { useState } from "react"

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

    return (
        <>
            <h2>Counter</h2>

            <p>{count}</p>

            <button onClick={decrementBtnClickHandler}>-</button>
            <button onClick={resetBtnClickHandler}>Reset</button>
            <button onClick={incrementBtnClickHandler}>+</button>
        </>

    )
}