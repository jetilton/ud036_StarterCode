# -*- coding: utf-8 -*-


class Movie:
    """
    Class Movie stores data about movies
    
    Params:
        
        title(str): Movie title
        poster_image_url(str): url for poster image
        trailer_youtube_url(str): url for youtube movie trailer
        
    Returns: object of type Movie
    """
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url







