export default function KillCounter(props) {
    let title = 'Kill Counter';

    if (props.count == 1) {
        return (
            <h3>First blood!</h3>
        )
    }

    if (props.count == 2) {
        title = 'Double kill!!'
    }

    return (
        <>
            {props.count == 3
                ? <h3>Triple Kill!!!</h3>
                : <h3>{title}</h3>
            }
        </>
        
    )
}