import { useEffect, useState, useRef } from "react";

export default function RefDemo() {
    const [counter, setCounter] = useState(0);
    const initialRenderRef = useRef(true);

    useEffect(() => {
        if (!initialRenderRef.current) {
            console.log('Update only');
        } else {
            console.log('Initial render')
            initialRenderRef.current = false;
        }
    }, [counter])

    return (
        <>
            <h1>Counter</h1>
            <p>{counter}</p>
            <button onClick={() => setCounter(c => c + 1)}>+</button>
        </>
    );
}