import media
import fresh_tomatoes

"""To create instances or objects of the movie class datatype and to pass
    the required information about the type Movie.
    Add all the movies objects to a list movies and pass this list to
    fresh_tomatoes.open() function which will be used to render the movie
    website page"""

toy_story = media.Movie(
                "Toy Story",
                "A story about the boy whose toys come to life",
                "https://www.movieposter.com/posters/archive/main/204/MPW-102287",  # NOQA
                "https://www.youtube.com/watch?v=4KPTXpQehio")

avatar = media.Movie(
                "Avatar",
                "A story of a marine who tries to save the alien world"
                "that he has learned to call home",
                "https://i.pinimg.com/236x/69/e6/61/69e6612f69c8f7638ccbfc36cf4cab15--film-connu-avatar-movie.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

titanic = media.Movie(
                "Titanic",
                "A ship of dreams, unsinkable ocean liner and a story of love",
                "https://titanicsound.files.wordpress.com/2014/11/titanic_movie-hd-1.jpg",  # NOQA
                "https://www.youtube.com/watch?v=2e-eXJ6HgkQ")

ratatouille = media.Movie(
                "Ratatouille",
                "A rat can also cook",
                "https://movieposters2.com/images/671363-b.jpg",
                "https://www.youtube.com/watch?v=c3sBBRxDAqk")

home_alone = media.Movie(
                "Home Alone",
                "An adventorous day about staying at Home all alone",
                "https://i.pinimg.com/736x/95/f5/ab/95f5ab9aaab5b15b61165ec01500a772--home-alone-movie-alone-movies.jpg",  # NOQA
                "https://www.youtube.com/watch?v=c3sBBRxDAqk")

the_mummy = media.Movie(
                "The Mummy",
                "An ancient Egyptian princess is awakened from her crypt"
                "beneath the desert, bringing with her malevolence grown over
                "millennia and terrors that defy human comprehension.",
                "https://images-na.ssl-images-amazon.com/images/I/7151Qmxd3pL._SY550_.jpg",  # NOQA
                "https://www.youtube.com/watch?v=h3ptPtxWJRs&feature=player_embedded")  # NOQA

movies = [
        toy_story,
        avatar,
        titanic,
        ratatouille,
        home_alone,
        the_mummy
        ]
fresh_tomatoes.open_movies_page(movies)
