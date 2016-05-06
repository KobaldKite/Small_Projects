import unittest
import os
import sort_files


class TestGeneral(unittest.TestCase):
    def setUp(self):
        temp_dir_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'to_sort')
        if not os.path.exists(temp_dir_name):
            os.makedirs(temp_dir_name)
        for file_name in ['a', 'b']:  # Filename can be generated dynamically in the loop
            with open(os.path.join(temp_dir_name, file_name), "wb") as out:
                out.seek(1000)
                out.write('\0')

    def test_sort(self):
        pass