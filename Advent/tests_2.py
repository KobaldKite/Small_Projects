import os
import unittest
import ad_2


TASKS = {
    'SILVER': 1,
    'GOLD': 2
}

SIZES_SAMPLES_GOOD = (
    ('10', '10', '6'),    # 500 paper, 632 ribbon
    ('-10', '10', '6'),   # Negative dimension, the box is ignored
    ('10', '10', '10'),   # 700 paper, 1040 ribbon
    ('10', '0', '10')     # Zero dimension value, the box is ignored
)

SIZES_SAMPLES_BAD = (
    ('10.5', '10', '6'),  # Not possible to convert to integer
    ('10', '10', '6.1')
)

SIZES_SAMPLES = (  # Code duplication. I don't think it's worth it to create a separate function.
    ('\n'.join(['x'.join(line) for line in SIZES_SAMPLES_GOOD]), 1200, 1672),
    ('\n'.join(['x'.join(line) for line in SIZES_SAMPLES_BAD]), -1, -1)
)

TEMP_FILE_NAMES = ['_'.join(['file', str(number)]) for number, _ in enumerate(SIZES_SAMPLES)]

RESULTS = (1200, 1672)

good_file = 'good_file'
bad_file = 'bad_file'


def clear():
    for test_file in (good_file, bad_file):
        if os.path.isfile(test_file):
            os.remove(test_file)


class TestGeneral(unittest.TestCase):
    def setUp(self):
        clear()
        for temp_file_name, sizes_sample in zip(TEMP_FILE_NAMES, SIZES_SAMPLES):
            with open(temp_file_name, 'w') as temp_file:
                temp_file.write(sizes_sample[0])

    def tearDown(self):
        clear()

    def test_whole(self):
        for temp_file_name, sizes_sample in zip(TEMP_FILE_NAMES, SIZES_SAMPLES):
            print temp_file_name
            sizes_list = ad_2.parse_size_file(temp_file_name)
            print sizes_list
            for task_type in ad_2.TYPE:
                print ad_2.wrap_boxes(sizes_list, task_type)
                self.assertEqual(ad_2.wrap_boxes(sizes_list, task_type),
                                 sizes_sample[TASKS.get(task_type)])


if __name__ == '__main__':
    unittest.main()

