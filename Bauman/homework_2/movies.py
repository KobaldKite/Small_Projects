import urllib

# http://python.aori.ru/data/movies.csv


'''movie id | movie title | release date | video release date | IMDb URL | unknown |
 Action | Adventure | Animation | Children's | Comedy | Crime | Documentary | Drama |
  Fantasy | Film-Noir | Horror | Musical | Mystery | Romance | Sci-Fi | Thriller | War | Western |'''


class MovieAdviser(object):
    def __init__(self):
        pass

    def get_data(self):
        raw_data = urllib.urlopen('http://python.aori.ru/data/movies.csv').read()
        print raw_data


def main():
    adviser = MovieAdviser()
    adviser.get_data()


if __name__ == '__main__':
    main()