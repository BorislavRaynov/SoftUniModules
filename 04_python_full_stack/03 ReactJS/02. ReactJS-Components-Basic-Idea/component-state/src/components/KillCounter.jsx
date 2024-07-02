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

    if (props.count > 10) {
        title = 'GodLike!'
    } else if (props.count > 5) {
        title = 'Unstoppable!'
    } else if(props.count > 3) {
         title = 'Multi kill!'
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