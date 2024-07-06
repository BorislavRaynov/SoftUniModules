import { useState } from 'react';
import './App.css'

function App() {
	const [movies, setMovies] = useState([
		'The Matrix',
		'Man of Steel',
		'Lord of t Rings',
		'The Case of Christ',
	]);

	const btnClickHandler = () => {
		setMovies((oldMovies) => {
			const newMovies = [...oldMovies];
			newMovies[2] = 'Harry Potter';
			newMovies.push('Avengers');
			newMovies.shift()

			return newMovies
		});
	};

	return (
		<>
			<h1>Movies</h1>

			{/* <ul>
				<li>{movies[0]}</li>
				<li>{movies[1]}</li>
				<li>{movies[2]}</li>
			</ul> */}

			<ul>
				{movies.map(movie => <li key={movie}>{movie}</li>)}
			</ul>

			<button onClick={btnClickHandler}>Change</button>
		</>
	)
}

export default App
