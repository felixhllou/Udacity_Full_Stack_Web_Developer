import webbrowser


class Movie():
    # This provides documentation about the class "Movie"
    """
    This class stores movie related information
    Attributes:
        title (String): movie's title
        poster_image_url (String): url that points to the movie's poster
        trailer_youtube_url (String): url that points the movie's trailer
        year (int): movie's release year
    """

    # Initialize and create space in memory for the object
    # instantiated with its attributes
    def __init__(self, title, poster_url, trailer_url, year):
        self.title = title
        self.poster_image_url = poster_url
        self.trailer_youtube_url = trailer_url
        self.year = year

    # override default string method and show movie title instead
    def __str__(self):
        return self.title

    # instance associated method
    def play_trailer(self):
        """ Allow playing the movie trailer """
        webbrowser.open(self.trailer_youtube_url)
