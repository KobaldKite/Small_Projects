import unittest
import os
import io
import articles_generator

ARTICLE_COUNT = 3

ARTICLE_DATABASE = {'articles': [
    {'title': u'aa', 'text': u'aa', 'topics': 'agrobiologia'},
    {'title': u'aa', 'text': u'ab', 'topics': 'astronomy'},
    {'title': u'ab', 'text': u'bb', 'topics': 'astronomy'},
    {'title': u'bb', 'text': u'ac', 'topics': 'astronomy'},
    {'title': u'ac', 'text': u'cc', 'topics': 'astronomy'}]}


class TestGeneral(unittest.TestCase):
    def setUp(self):
        self.article_database = articles_generator.ArticleDataBase(ARTICLE_COUNT)
        self.file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_file')
        self.path_json = '.'.join([self.file_path, 'json'])
        self.path_html = '.'.join([self.file_path, 'html'])

    def tearDown(self):
        if os.path.isfile(self.path_json):
            os.remove(self.path_json)
        if os.path.isfile(self.path_html):
            os.remove(self.path_html)

    def test_print_to_file(self):
        self.article_database.print_to_file(self.path_json)
        with io.open(self.path_json) as json_file:
            data = articles_generator.json.load(json_file)
            self.assertIsInstance(data.get('articles'), list)
            for article_number in xrange(ARTICLE_COUNT):
                self.assertIsInstance(data.get('articles')[article_number].get('text'), unicode)
                self.assertIsInstance(data.get('articles')[article_number].get('title'), unicode)
                self.assertIsInstance(data.get('articles')[article_number].get('topics'), list)
            print data

    def test_filter_titles(self):
        self.article_database.json_data = ARTICLE_DATABASE
        self.assertEqual(
            self.article_database.filter_titles('b', 'title_only'),
            ARTICLE_DATABASE.get('articles')[2:4])
        self.assertEqual(
            self.article_database.filter_titles('b', 'title_and_text'),
            ARTICLE_DATABASE.get('articles')[1:4])

    def test_output_articles(self):
        self.article_database.json_data = ARTICLE_DATABASE
        self.article_database.output_articles(2, 2, self.file_path)
        with io.open(self.path_html) as html_file:
            self.assertEqual(html_file.read(),
                             '<h1>ab</h1><div>bb</div><h1>bb</h1><div>ac</div>')