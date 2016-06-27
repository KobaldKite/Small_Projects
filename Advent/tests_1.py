import os
import unittest
import ad_1


TASKS = {
    'SILVER': 1,
    'GOLD': 2
}

DIRECTIONS_SAMPLES = (
    ('(())())(', 0, 7),          # Location = 0, cellar = 7
    ('((())())())()', -1, 11),   # Location = -1, cellar = 11
    (')()()(', 0, 1),            # Location = 0, cellar = 1 (first)
    ('(((()((', 5, -1)           # Location = 5, cellar = -1 (never)
)

TEMP_FILE_NAMES = (
    ['_'.join(['file', str(number)]) for number, _ in enumerate(DIRECTIONS_SAMPLES)]
)


def clear():
    for temp_file_name in TEMP_FILE_NAMES:
        if os.path.isfile(temp_file_name):
            os.remove(temp_file_name)


class TestGeneral(unittest.TestCase):
    def setUp(self):
        clear()
        for sample_number, direction_sample in enumerate(DIRECTIONS_SAMPLES):
            with open(TEMP_FILE_NAMES[sample_number], 'w') as temp_file:
                temp_file.write(direction_sample[0])

    def tearDown(self):
        clear()

    def test_general(self):
        for temp_file, direction_sample in zip(TEMP_FILE_NAMES, DIRECTIONS_SAMPLES):
            for task_type in ad_1.TYPE:
                santa = ad_1.Santa(task_type)
                self.assertEqual(santa.do_the_job(temp_file),
                                 direction_sample[TASKS.get(task_type)])


if __name__ == '__main__':
    unittest.main()