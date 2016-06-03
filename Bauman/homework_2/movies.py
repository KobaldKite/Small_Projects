import urllib
import csv
import collections
import argparse
import random
import requests
import bs4
import fuzzywuzzy

HEADER = ('movie id', 'movie title', 'release date', 'video release date',
          'IMDb URL', 'unknown', 'Action', 'Adventure', 'Animation', 'Children\'s',
          'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir',
          'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western')
MOVIE_SEARCH_DEPTH = 10  # Determines how far we go to find similar movies.


# DONE
def get_data():
    movie_file = urllib.urlopen('http://python.aori.ru/data/movies.csv')
    movie_list = csv.DictReader(movie_file, HEADER, delimiter='|')
    return movie_list


# DONE
def get_random_movie(movie_list):
    try:
        suggested = random.choice(movie_list)
    except IndexError:
        print 'There is no movies that satisfy your criteria.'
        return ''
    else:
        return suggested


# Probably add switching to another page HERE
def parse_movie_page(movie):
    """
    :param movie: dict; line of the csv file
    :return: soup object; page of the sent movie
    """
    #movie_url = movie.get('IMDb URL')
    #print movie_url
    #movie_raw_html = requests.get(movie_url).text
    #movie_page_soup = bs4.BeautifulSoup(movie_raw_html, 'html.parser')
    movie_page_soup = check_movie_page(movie)
    return movie_page_soup


def check_movie_page(movie):
    movie_url = movie.get('IMDb URL')
    movie_raw_html = requests.get(movie_url).text
    movie_page_soup = bs4.BeautifulSoup(movie_raw_html, 'html.parser')
    try:
        rating = movie_page_soup.find(itemprop='ratingValue').contents[0]  # use another sign
    except AttributeError:
        print movie_url
        similar_list = movie_page_soup.find_all('result_text')[:5]
        print similar_list
        # Use fuzzywuzzy to find the most similar
        # Assign new soup_movie_page value afterwards
    return movie_page_soup

# Class = findList
# Class = result_text

# Alternative way:
# if it's not possible to get to the movie page, display another movie


def find_the_most_similar(similar_list, original_title):
    pass
    # should it return the soup object?


def get_rating_from_soup(soup_movie_page):
    """
    :param:
    :return: movie rating (string?)
    """
    try:
        rating = soup_movie_page.find(itemprop='ratingValue').contents[0]
    except AttributeError:
        print "Can't find rating"
        rating = 'N/A'
    return rating


def get_image_from_soup(soup_movie_page):
    """
    :param:
    :return: poster image url
    """
    try:
        image = soup_movie_page.find(class_='poster').a.img['src']
    except AttributeError:
        print "Can't find image"
        image = 'N/A'  # Placeholder image here
    return image


def count_by_year(movie_list):
    """
    :param movie_list: list of dicts
    :return: ???
    """
    dates = []
    for movie in movie_list:
        dates.append(movie.get('release date').split('-')[-1])  # Use datetime module instead
    return collections.Counter(dates)


def get_movies_by_year_and_genre(movie_list, genre, year):
    """
    :param movie_list: list of dicts
    :param genre: string; one of mentioned in the csv header
    :param year: integer or string
    :return: list of dicts; movies of the received year and genre
    """
    selected_movies = []
    for movie in movie_list:
        if movie.get('release date').split('-')[-1] == str(year) and\
                movie.get(genre) == '1':
            selected_movies.append(movie)
    return selected_movies


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--genre', action='store', dest='genre', default='Drama')
    parser.add_argument('--year', action='store', dest='year', default='1996')
    return parser.parse_args()


def main():
    arguments = parse_arguments()
    movies = get_data()
    selected_movies = get_movies_by_year_and_genre(movies, arguments.genre, arguments.year)
    print len(selected_movies)
    movie = get_random_movie(selected_movies)
    soup = parse_movie_page(movie)
    print get_rating_from_soup(soup)
    print get_image_from_soup(soup)


if __name__ == '__main__':
    main()