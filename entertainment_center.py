import media
import fresh_tomatoes

# Instantiating movies class with proper information.
annie_hall = media.Movie("Annie Hall",
                        "Woody Allens best movie",
                        "https://upload.wikimedia.org/wikipedia/en/e/e6/Anniehallposter.jpg",
                        "https://www.youtube.com/watch?v=TBzHphcc2Jw")

oldboy = media.Movie("Oldboy", "A man about revange",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BMTI3NTQyMzU5M15BMl5BanBnXkFtZTcwMTM2MjgyMQ@@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
                     "https://www.youtube.com/watch?v=D89OHw0VsYM")

adaptation = media.Movie("Adaptation","It's complicating",
                         "https://upload.wikimedia.org/wikipedia/en/5/5e/Adaptation._film.jpg",
                         "https://www.youtube.com/watch?v=yZA2BlRH-6o")

# Making a list of movies so that it can be fed into fresh_tomatoes
movies = [annie_hall, oldboy, adaptation]

# Open movies website
fresh_tomatoes.open_movies_page(movies)
