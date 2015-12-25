import urllib
import random
import argparse


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
ARTICLE_NUMBER = 10  # The total number of generated articles
MIN_TOPIC_NUMBER = 1  # Every article can have up to three themes
MAX_TOPIC_NUMBER = 3
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


class ArticleDatabase:
    def __init__(self):
        self.json_data = {'articles':
                          [{'title': generate_title(),
                            'topics': topics,
                            'text': generate_article(topics)}
                           for topics in (pick_random_topics() for article_counter
                                          in xrange(ARTICLE_NUMBER))]}

    def print_to_file(self, path='articles.json'):  # Use 'check' to print data in a simpler format..
        pass  # No JSON so far
        #with open(path, 'w') as json_file:
        #    json.dump(self.json_data, json_file, ensure_ascii=False, encoding='utf-8')

    def check(self, path='test.txt'):  # Generates a file that helps me with debugging
        with open(path, 'w') as test_file:
            for current_article in self.json_data.get('articles'):
                test_file.write('\n'.join((current_article.get('title'),
                                           '\n'.join(current_article.get('topics')),
                                           current_article.get('text'),
                                           '\n'))
                                .encode('utf-8'))  # TODO: find a better way

    def output_articles(self, displayed_page=1, articles_per_page=1, path='console'):
        articles = self.json_data.get('articles')
        selected_articles = articles[(displayed_page + PAGE_SHIFT) * articles_per_page:
                                     displayed_page * articles_per_page]
        if path == 'console':
            for current_article in selected_articles:
                print current_article.get('title')
                print current_article.get('topics')
                print current_article.get('text')  # TODO: find a better way
        else:
            self.check(path)  # Change to 'print_to_file' later

    def filter_titles(self, request, search_type):
        result = []
        for article in self.json_data.get('articles'):
            if (request in article.get('title')) or\
               (request in article.get('text') and search_type == 'title_and_text'):
                result.append(article)  # TODO: find a better condition
        return result

    def find_articles(self, request, search_type='title_only'):
        if search_type in SEARCH_TYPES:
            return self.filter_titles(request, search_type)
        else:
            print "You can use only 'title_only' or 'title_and_text' as search behavior types."
            return []


def main(args):
    articles = ArticleDatabase()
    articles.output_articles(int(args.displayed_page), int(args.articles_per_page), args.path)
    articles.find_articles(args.request, args.search_type)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', action='store', dest='search_type', default='title_only')
    parser.add_argument('-p', action='store', dest='path', default='console')
    parser.add_argument('-r', action='store', dest='request', default='')
    parser.add_argument('-dp', action='store', dest='displayed_page', default='1')
    parser.add_argument('-ap', action='store', dest='articles_per_page', default='0')
    arguments = parser.parse_args()
    print arguments
    main(arguments)
