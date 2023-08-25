from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def register_user(self, username: str, age: int):
# Creates an instance of the User class with the given username and age

        for u in self.users_collection:
            if u.username == username:
                raise Exception("User already exists!")
        else:
            user = User(username, age)
            self.users_collection.append(user)
            return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        user = [u for u in self.users_collection if u.username == username]
        if user:
            user = user[0]
        else:
            raise Exception("This user does not exist!")

# Only the owner of the movie given can edit it.
        if movie.owner.username != user.username:
        # if movie.owner != user:
            raise Exception(f"{username} is not the owner of the movie {movie.course_name}!")

        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")

        user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f"{username} successfully added {movie.course_name} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        user = [u for u in self.users_collection if u.username == username][0]

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.course_name} is not uploaded!")

        if movie.owner.username != user.username:
        # if movie.owner != user:
            raise Exception(f"{username} is not the owner of the movie {movie.course_name}!")

        for key, value in kwargs.items():
            if key == "year":
                movie.year = value
            if key == "title":
                movie.course_name = value
            if key == "age_restriction":
                movie.age_restriction = value

        return f"{username} successfully edited {movie.course_name} movie."

    def delete_movie(self, username: str, movie: Movie):
        user = [u for u in self.users_collection if u.username == username][0]
        # movie = [m for m in self.movies_collection if m.username == username][0]

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.course_name} is not uploaded!")

        if movie.owner.username != user.username:
        # if movie.owner != user:
            raise Exception(f"{username} is not the owner of the movie {movie.course_name}!")

        self.movies_collection.remove(movie)
        user.movies_owned.remove(movie)
        return f"{username} successfully deleted {movie.course_name} movie."

    def like_movie(self, username: str, movie: Movie):
        user = [u for u in self.users_collection if u.username == username][0]

        if movie.owner.username == user.username:
        # if movie.owner == user:
            raise Exception(f"{username} is the owner of the movie {movie.course_name}!")

        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.course_name}!")

        movie.likes += 1
        user.movies_liked.append(movie)
        return f"{username} liked {movie.course_name} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = [u for u in self.users_collection if u.username == username][0]
        # movie = [m for m in self.movies_collection if m.username == username][0]

        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.course_name}!")

        movie.likes -= 1
        user.movies_liked.remove(movie)
        return f"{username} disliked {movie.course_name} movie."

    def display_movies(self):
        if not self.movies_collection:
            return "No movies found."

        result = []

        sorted_movies = sorted(self.movies_collection, key=lambda curr_movie: (-curr_movie.year, curr_movie.course_name))
        for movie in sorted_movies:
            result.append(movie.details())

        return "\n".join(result)

    def __str__(self):
        result = []
        if self.users_collection:
            result.append(f"All users: {', '.join([user.username for user in self.users_collection])}")
        else:
            result.append("All users: No users.")

        if self.movies_collection:
            result.append(f"All movies: {', '.join([movie.course_name for movie in self.movies_collection])}")
        else:
            result.append("All movies: No movies.")

        return "\n".join(result)


