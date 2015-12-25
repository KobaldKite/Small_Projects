import unittest
import argparse
import subprocess
import ad_1


class TestArguments(unittest.TestCase):
    pass


class TestFileWork(unittest.TestCase):
    # Create a string
    # Create a file
    # Write string to the file
    # Read the file
    # Compare strings
    # ----- does it sound fair?
    pass


class TestSymbolParse(unittest.TestCase):
    # Mostly several cases with different results. Use StringIO here?
    def create_test_file(self, test_string):
        with open('test_file', 'w') as test_file:
            test_file.write(test_string)

    def test_ground_levels(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-f', action='store', dest='file_path', default='')
        parser.add_argument('-t', action='store', dest='type', default='SILVER')
        args = parser.parse_args(['-f', 'test_file'])

        # Above ground
        self.create_test_file('((()(()(')
        santa = ad_1.Santa(args)
        santa.follow_directions()

        process = subprocess.Popen(['echo', '"Hello!"'], stdout=subprocess.PIPE)  # Change [.] to the function run?
        line = process.stdout.readline()
        print line

        # Ground floor
        # Under ground
        pass

    pass