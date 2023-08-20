from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def find_user_in_collection(self, username):
        for user in self.users_collection:
            if user.username == username:
                return user

    def find_movie_in_collection(self, movie: Movie):
        for m in self.movies_collection:
            if m.title == movie.title:
                return m

    def register_user(self, username: str, age: int):
        if self.find_user_in_collection(username):
            raise Exception("User already exists!")

        new_user = User(username, age)
        self.users_collection.append(new_user)
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        user = self.find_user_in_collection(username)
        if not user:
            raise Exception("This user does not exist!")

        if self.find_movie_in_collection(movie):
            raise Exception("Movie already added to the collection!")

        if username != movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        self.movies_collection.append(movie)
        user.movies_owned.append(movie)
        return f'{username} successfully added {movie.title} movie.'

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        if not self.find_movie_in_collection(movie):
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for attribute, value in kwargs.items():
            setattr(movie, attribute, value)
        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        if not self.find_movie_in_collection(movie):
            raise Exception(f"The movie {movie.title} is not uploaded!")
        if movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        self.movies_collection.pop(self.movies_collection.index(movie))
        user = self.find_user_in_collection(username)
        user.movies_owned.pop(user.movies_owned.index(movie))
        return f'{username} successfully deleted {movie.title} movie.'

    def like_movie(self, username: str, movie: Movie):
        if movie.owner.username == username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        user = self.find_user_in_collection(username)
        for m in user.movies_liked:
            if m.title == movie.title:
                raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        user.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = self.find_user_in_collection(username)

        for i, m in enumerate(user.movies_liked):
            if m.title == movie.title:
                movie.likes -= 1
                user.movies_liked.pop(i)
                break
        else:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if not self.movies_collection:
            return "No movies found."

        result_str = []
        for movie in sorted(self.movies_collection, key=lambda x: (-x.year, x.title)):
            result_str.append(movie.details())
        return '\n'.join(result_str)

    def __str__(self):
        if len(self.users_collection) == 0:
            users = 'No users.'
        else:
            users = ', '.join([user.username for user in self.users_collection])
        if len(self.movies_collection) == 0:
            movies = 'No movies.'
        else:
            movies = ', '.join([movie.title for movie in self.movies_collection])

        return f'All users: {users}\nAll movies: {movies}'
