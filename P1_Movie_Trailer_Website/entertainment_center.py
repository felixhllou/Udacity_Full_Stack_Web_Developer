import fresh_tomatoes
import media
import csv


def fetch_movies(file):
    """ fetch movie metadata and return a list of movie objects """
    movies = []
    with open(file, 'r') as movie_metadata:
        dict_reader = csv.DictReader(movie_metadata)
        for movie in dict_reader:
            movies.append(media.Movie(
                title=movie['name'],
                poster_url=movie['poster'],
                trailer_url=movie['trailer'],
                year=movie['year']))
    return movies


def main():
    """ subroutine if run as the main program """
    movies = fetch_movies('movies_data/movies_data.csv')

    # build the HTML
    fresh_tomatoes.open_movies_page(movies)

if __name__ == '__main__':
    main()
