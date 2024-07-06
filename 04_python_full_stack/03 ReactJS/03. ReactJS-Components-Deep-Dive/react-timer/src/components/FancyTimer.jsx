import { useState, useEffect } from "react";

export default function FancyTimer() {
    const [time, setTime] = useState(0)

    useEffect(() => {
        setInterval(() => {
            setTime(oldTime => oldTime + 1)
        }, 1000);
    }, [])

    const addSecondsHandler = () => {
        setTime(prevTime => prevTime + 10);
    };

    return (
        <>
            <h1>Fancy Timer</h1>
            <div>{time}</div>
            <button onClick={addSecondsHandler}>Add Seconds</button>
        </>
    );
};