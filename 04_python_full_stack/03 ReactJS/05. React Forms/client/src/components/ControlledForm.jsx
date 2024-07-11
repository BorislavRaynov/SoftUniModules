import { useState } from "react";

export default function ControlledForm() {
    const [user, setUser] = useState({
        username: 'Pesho',
    })

    const formSubmitHandler = (e) => {
        e.preventDefault();

        console.log('Form submited')
    }

    return (
        <>
            <h1>Controlled Form</h1>

            <form action="#" onSubmit={formSubmitHandler}>
                <div>
                    <label htmlFor="username">Username</label>
                    <input type="text" name="username" id="username" defaultValue={user.username} />
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