import urllib
import random
import argparse
import json
import io


AVAILABLE_ARTICLE_THEMES = [
    'astronomy',
    'geology',
    'gyroscope',
    'literature',
    'marketing',
    'mathematics',
    'music',
    'polit',
    'agrobiologia',
    'law',
    'psychology',
    'geography',
    'physics',
    'philosophy',
    'chemistry',
    'estetica'
]
SEARCH_TYPES = [
    'title_only',
    'title_and_text'
]
MIN_TOPIC_NUMBER = 1
MAX_TOPIC_NUMBER = 3  # Every article can have up to three themes
PAGE_SHIFT = -1  # Required to find the right number of articles, used in list slices.


def generate_title():
    raw_title = urllib.urlopen('https://referats.yandex.ru/creator/write/').read()
    return raw_title.decode('utf-8').capitalize()


def generate_article(themes):
    for topic in themes:
        assert topic in AVAILABLE_ARTICLE_THEMES
    url_template = 'https://referats.yandex.ru/referats/write/?%s'
    url = url_template % urllib.urlencode({'t': '+'.join(themes)})
    raw_text = urllib.urlopen(url).read().decode('utf-8')
    article = '<p>%s' % '<p>'.join(raw_text.split('<p>')[1:])
    return article


def pick_random_topics():
    return tuple(random.sample(AVAILABLE_ARTICLE_THEMES,
                               random.randint(MIN_TOPIC_NUMBER, MAX_TOPIC_NUMBER)))


def write_to_html(article_list, path='selected_articles.html'):
    with io.open(path, 'w',  encoding='utf8') as articles_file:
        for article in article_list:
            articles_file.write(''.join(['<h1>', article.get('title'), '</h1>']))
            articles_file.write(''.join(['<div>', article.get('text'), '</div>']))


class ArticleDataBase:
    def __init__(self, article_number=10):
        self.json_data = {'articles':
                          [{'title': generate_title(),
                            'topics': topics,
                            'text': generate_article(topics)}
                           for topics in (pick_random_topics() for article_counter
                                          in xrange(int(article_number)))]}

    def print_to_file(self, path='articles.json'):
        data = json.dumps(self.json_data, ensure_ascii=False)
        with io.open(path, 'w', encoding='utf8') as json_file:
            json_file.write(data)

    def output_articles(self, displayed_page=1, articles_per_page=1, path='console'):
        """
        Article list gets divided into pages, like a book;
        each page contains a certain number or articles.
        For example, if you want to see a third page,
        where each page contains two articles, you'll see articles 5 and 6.
        :param displayed_page: page number, starts from 1
        :param articles_per_page: how many articles are on a page
        :param path: either 'console' or path to a file without extension;
               in the second case, an html file containing selected articles is created
        :return: list of articles on a selected page; empty list if there were errors
        """
        articles = self.json_data.get('articles')
        try:
            selected_articles = articles[(displayed_page + PAGE_SHIFT) * articles_per_page:
                                         displayed_page * articles_per_page]
        except (IndexError, ValueError):
            print 'Not a valid number!'
            selected_articles = []

        if path == 'console':
            for current_article in selected_articles:
                print current_article.get('title')
                print current_article.get('text')
        else:
            path_html = '.'.join([path, 'html'])
            write_to_html(selected_articles, path_html)

    def filter_titles(self, request, search_type):
        """
        :param request: symbol combination that is required to present in articles user is looking for
        :param search_type: where the aforementioned combination is looked for;
               can be set to either 'title_only' or 'text_and_title'
        :return: the list of articles containing the 'request' combination in title or text;
                 empty list if there were errors
        """
        result = []
        for article in self.json_data.get('articles'):
            if (request in article.get('title')) or\
               (request in article.get('text') and search_type == 'title_and_text'):
                result.append(article)
        return result

    def find_articles(self, request, search_type='title_only'):
        if search_type in SEARCH_TYPES:
            return self.filter_titles(request, search_type)
        else:
            print "You can use only 'title_only' or 'title_and_text' as search behavior types."
            return []


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', action='store', dest='article_number', default=10)
    parser.add_argument('-p', action='store', dest='path', default='console')
    parser.add_argument('-dp', action='store', dest='displayed_page', default='1')
    parser.add_argument('-ap', action='store', dest='articles_per_page', default='0')
    parser.add_argument('-r', action='store', dest='request', default='')
    parser.add_argument('-s', action='store', dest='search_type', default='title_only')
    return parser.parse_args()


def main():
    arguments = parse_arguments()
    print arguments

    articles = ArticleDataBase(arguments.article_number)
    articles.print_to_file()
    articles.output_articles(int(arguments.displayed_page),
                             int(arguments.articles_per_page),
                             arguments.path)
    articles.find_articles(arguments.request, arguments.search_type)


if __name__ == '__main__':
    main()
