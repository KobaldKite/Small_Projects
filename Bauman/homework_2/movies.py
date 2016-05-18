import urllib
import csv
import collections
import argparse
import random
import requests
import bs4

HEADER = ('movie id', 'movie title', 'release date', 'video release date',
          'IMDb URL', 'unknown', 'Action', 'Adventure', 'Animation', 'Children\'s',
          'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir',
          'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western')


def get_data():
    movie_file = urllib.urlopen('http://python.aori.ru/data/movies.csv')
    movie_dict_reader = csv.DictReader(movie_file, HEADER, delimiter='|')
    return movie_dict_reader


def get_random_movie(movie_list):
    try:
        suggested = random.choice(movie_list)
    except IndexError:
        print 'There is no movies that satisfy your criteria.'
        return ''
    else:
        return suggested.get('movie title'), get_movie_rating(suggested)


def get_movie_rating(movie):
    movie_url = movie.get('IMDb URL')
    movie_page_html = requests.get(movie_url).text
    return movie_page_html


def get_image(page='http://www.imdb.com/title/tt0115956/'):
    raw_html = requests.get(page).text
    soup = bs4.BeautifulSoup(raw_html, 'html.parser')
    image = soup.find(class_='poster').a.img['src']
    return image


class MovieAdviser(object):
    def __init__(self):
        self.movies = get_data()

    def count_by_year(self):
        dates = []
        for movie in self.movies:
            dates.append(movie.get('release date').split('-')[-1])  # Use datetime module instead
        return collections.Counter(dates)

    def get_movies_by_year_and_genre(self, genre, year):
        selected_movies = []
        for movie in self.movies:
            if movie.get('release date').split('-')[-1] == year and\
                    movie.get(genre) == '1':
                selected_movies.append(movie)
        return selected_movies


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--genre', action='store', dest='genre', default='War')
    parser.add_argument('--year', action='store', dest='year', default='1996')
    return parser.parse_args()


def main():
    arguments = parse_arguments()
    adviser = MovieAdviser()
    selected_movies = adviser.get_movies_by_year_and_genre(arguments.genre, arguments.year)
    print len(selected_movies)
    print get_random_movie(selected_movies)
    print selected_movies
    print get_image()


if __name__ == '__main__':
    main()