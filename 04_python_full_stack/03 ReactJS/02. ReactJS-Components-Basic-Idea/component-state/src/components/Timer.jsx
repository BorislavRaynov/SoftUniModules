import { useState } from "react";

export default function Timer() {
    const [count, setCount] = useState(0)

    setTimeout(() => {
        setCount(count + 1);
    }, 1000)

    return (
        <>
            <h2>Counter</h2>

            <p>{count}</p>
        </>
    )
}