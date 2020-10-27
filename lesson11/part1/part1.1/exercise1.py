def favorite_movie(movie_title):
    if "Batman" in str(movie_title).capitalize()  :
        print("good choice!")
    else:
        print("awful taste...")

favorite_movie("Batman")
favorite_movie("Star Wars")
favorite_movie("Batman and Robin")