import unittest
import os
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
        self.ArticleDataBase = articles_generator.ArticleDataBase(ARTICLE_COUNT)
        self.JSONFilename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_file.json")

    def tearDown(self):
        pass

    def test_print_to_file(self):
        self.ArticleDataBase.print_to_file(self.JSONFilename)
        with open(self.JSONFilename) as json_file:
            data = articles_generator.json.load(json_file)
            self.assertIsInstance(data.get('articles'), list)
            for article_number in xrange(ARTICLE_COUNT):
                self.assertIsInstance(data.get('articles')[article_number].get('text'), unicode)
                self.assertIsInstance(data.get('articles')[article_number].get('title'), unicode)
                self.assertIsInstance(data.get('articles')[article_number].get('topics'), list)
            print data

    def test_filter_titles(self):
        self.ArticleDataBase.json_data = ARTICLE_DATABASE
        self.assertEqual(
            self.ArticleDataBase.filter_titles('b', 'title_only'),
            ARTICLE_DATABASE.get('articles')[2:4])
        self.assertEqual(
            self.ArticleDataBase.filter_titles('b', 'title_and_text'),
            ARTICLE_DATABASE.get('articles')[1:4])

    def test_output_articles(self):
        pass