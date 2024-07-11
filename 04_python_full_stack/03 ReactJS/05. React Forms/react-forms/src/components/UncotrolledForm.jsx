import { useState } from "react";

export default function UncotrolledForm() {
    const [user, setUser] = useState({})

    const formSubmitHandler = (e) => {
        console.log('Form submited')
    }

    return (
        <>
            <h1>Uncontrolled Form</h1>

            <form action="#" onClick={formSubmitHandler}>
                <div>
                    <label htmlFor="username">Username</label>
                    <input type="text" name="username" id="username" />
                </div>
                <div>
                    <label htmlFor="password">Password</label>
                    <input type="password" name="password" id="password" />
                </div>  
                <div>
                    <input type="submit" value="login" />
                </div>
            </form>
        </>
    );
}