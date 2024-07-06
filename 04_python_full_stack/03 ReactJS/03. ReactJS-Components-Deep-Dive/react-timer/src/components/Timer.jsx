import { useState } from "react";

export default function Timer() {
    const [time, setTime] = useState(0)

    setTimeout(() => {
        setTime(prevTime => prevTime + 1)
    }, 1000);

    return (
        <>
            <h1>Timer</h1>
            <div>{time}</div>
        </>
    )
}