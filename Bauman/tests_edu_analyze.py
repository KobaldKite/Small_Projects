import unittest
import os
import io
import json
import edu_analyze


JSON_DATA = [{'Lat': 55, 'Lon': 37, 'Cells': {'name': 'N', 'okrug': okrug}}
             for okrug in ('a', 'b', 'a', 'c', 'b', 'a', 'd', 'e', 'f')]


class TestGeneral(unittest.TestCase):
    def test_path(self):
        with io.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'temp_file.json'), 'wb') as local_file:
            json.dump(JSON_DATA, local_file)
            pass
