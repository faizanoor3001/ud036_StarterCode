import webbrowser

class Movie():
    """ This class provides a way to store movie related information i.e.to define a movie type object"""
    #constructor to initialise the movie type variables
    def __init__(self,movie_title,movie_story_line,poster_image,trailer_youtube):
        self.title = movie_title
        self.story_line = movie_story_line
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    #the function takes self as a parameter always , used to show the trailor of a given movie object
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
