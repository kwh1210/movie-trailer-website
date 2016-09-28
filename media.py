import webbrowser


class Movie():
    """This class provides a way to store movie related information"""

    # Possible rating values.
    VALID_RATING = ["G","PG","PG-13","R"]

    # Constructor. Requires 3 non-self argument
    def __init__(self,movie_title, movie_storyline,
                 poster_image, trailer_youtube):

        # Initializing the member variables
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Member function to show trailer on youtube.
    def show_trailer(self):

        # Simple function from webbrowser module
        webbrowser.open(self.trailer_youtube_url)
