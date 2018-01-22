import webbrowser


class Movie():
    """ This class provides a way to store movie related information
        i.e.to define a movie type object

        Args:
            movie_title(str): Movie's Title
            movie_story_line : Movie Story Line
            poster_image : Box art image of the movie
            trailer_youtube : Link to the You tube URL


        Methods:
            show_trailer(): Show the trailer by opening the URL provided in the
            trailer youtube URL.
    """
    def __init__(
                self, movie_title,
                movie_story_line,
                poster_image,
                trailer_youtube
                ):
                """ constructor to initialize the instance variables of a class

                    Args:
                """
                self.title = movie_title
                self.story_line = movie_story_line
                self.poster_image_url = poster_image
                self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """The show_trailer() is used to show the trailor of a given movie object
        in a web browser.

        Returns None.
        OPens a web browser window
        """
        webbrowser.open(self.trailer_youtube_url)
