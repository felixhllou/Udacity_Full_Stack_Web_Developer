import webbrowser

class Movie():
    """
    A class to store movie info
    """                  
    def __init__(self, title, poster_url, trailer_url, year):
        self.title = title
        self.poster_image_url = poster_url
        self.trailer_youtube_url = trailer_url
        self.year = year

    # override default string method and show movie title instead
    def __str__(self):
        return self.title

    def play_trailer(self):
        """
        A method associated with the class which allows playing the movie trailer
        """
        webbrowser.open(self.trailer_youtube_url)