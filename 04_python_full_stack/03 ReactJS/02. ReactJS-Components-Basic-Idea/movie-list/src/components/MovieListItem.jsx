export default function MovieListItem(props) {
    return(
        <li style={{color: 'pink'}}>
            <a href={props.url || '#'} target="blank">
                {props.children}
            </a>
        </li>
    )
}