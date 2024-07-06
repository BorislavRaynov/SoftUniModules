import { useState, useEffect } from "react";

export default function Effect() {
    const [count, setCount] = useState(0)

    useEffect(() => {
        console.log('Initial Render')
    }, [])

    useEffect(() => {
        console.log('Update Counter')
    }, [count])

    return (
            <h2>Effect</h2>
    );
};