import unittest
import os
import io
import json
import edu_analyze
import urlparse, urllib


JSON_DATA = [{'Lat': 55, 'Lon': 37, 'Cells': {'name': 'N', 'okrug': okrug}}
             for okrug in ('a', 'b', 'a', 'd', 'b', 'a', 'c', 'e', 'f')]


class TestGeneral(unittest.TestCase):
    def setUp(self):
        self.test_file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            'temp_file.json')
        with io.open(self.test_file_path, 'wb') as local_file:
            json.dump(JSON_DATA, local_file)

    def tearDown(self):
        if os.path.isfile(self.test_file_path):
            os.remove(self.test_file_path)

    def test_path_open(self):
        district_list = edu_analyze.get_district_list('path', self.test_file_path)
        self.assertEqual(len(district_list), 9)

    def test_url_open(self):
        test_file_url = urlparse.urljoin(
            'file:', urllib.pathname2url(self.test_file_path))
        district_list = edu_analyze.get_district_list('url', test_file_url)
        self.assertEqual(len(district_list), 9)

    def test_most_common(self):
        district_list = edu_analyze.get_district_list('path', self.test_file_path)
        common_districts = edu_analyze.select_most_common(district_list, 3)
        self.assertEqual(common_districts[1], 'b')
        self.assertEqual(common_districts[2], 'c')  # Ensures alphabetical order for tied most common
