import MovieList from './components/MovieList'
import './App.css'

function App() {
	const movies = [
		'The Matrix',
		'Man of Steel',
		'Lord of the Rings',
		'Case for Christ',
	];

    return (
		<>
			<MovieList movies={movies}/>
		</>
  	)
}

export default App
