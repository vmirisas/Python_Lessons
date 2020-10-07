fav_movies = ["movie1", "movie3", "movie4", "movie2"]
new_movie = input("type a new favorite movie: ")
print(fav_movies)
if new_movie in fav_movies:
    print("this movie is already in your favourites")
else:
    fav_movies.append(new_movie)
fav_movies.sort()
print(fav_movies)
print(len(fav_movies))