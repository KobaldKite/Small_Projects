import unittest
import os
import shutil
import run_sort_files

SORT_METHODS = [
    'honest',
    'cheat'
]

class TestGeneral(unittest.TestCase):
    def setUp(self):
        """
        Four files of different size are created.
        In size descending order, they are a > d > c > b.
        """
        self.temp_dir_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'to_sort')
        if not os.path.exists(self.temp_dir_name):
            os.makedirs(self.temp_dir_name)
        file_names_enum = list(enumerate(['b', 'c', 'd', 'a'], start=1))
        for test_file in file_names_enum:
            with open(os.path.join(self.temp_dir_name, test_file[1]), "wb") as out:
                out.seek(int(test_file[0]) * 1000)
                out.write('\0')

    def tearDown(self):
        shutil.rmtree(self.temp_dir_name)

    def check_sorted(self, method):
        sorted_files = run_sort_files.sort_files(self.temp_dir_name, method)
        if method not in SORT_METHODS:
            self.assertEqual(sorted_files, -1)
        else:
            self.assertEqual(sorted_files[0][-1], 'a')
            self.assertEqual(sorted_files[2][-1], 'c')

    def test_honest(self):
        self.check_sorted(SORT_METHODS[0])

    def test_cheat(self):
        self.check_sorted(SORT_METHODS[1])

    def test_wrong_method(self):
        self.check_sorted('wrong_argument')