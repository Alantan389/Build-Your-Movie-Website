import webbrowser
"""The module provideds a interface to allow displaying
web-based documents to users."""


class Movie(object):
"""The class create a space to store movie details"""
    def __init__(self,movie_title,
                 movie_storyline,poster_image,
                 trailer_youtube,movie_release_date,movie_director):
        """Initialize the movie class instance variables"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release_date = movie_release_date
        self.director = movie_director
        """I have created six instance variables."""

    def show_trailer(self):
        '''This function make the the youtube video playable in the website '''
         webbrowser.open(self.trailer_youtube_url)
