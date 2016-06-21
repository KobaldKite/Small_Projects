import os
import unittest
import ad_2


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
        with open(good_file, 'w') as good:
            lines = ['x'.join(line) for line in SIZES_SAMPLES_GOOD]
            good.write('\n'.join(lines))
        with open(bad_file, 'w') as bad:  # Is it worth it to use a loop instead?
            lines = ['x'.join(line) for line in SIZES_SAMPLES_BAD]
            bad.write('\n'.join(lines))

    def tearDown(self):
        clear()

    def test_wrap_good(self):
        sizes_list = ad_2.parse_size_file(good_file)
        for task_number, task_type in enumerate(ad_2.TYPE):
            wrap = ad_2.wrap_boxes(sizes_list, task_type)
            self.assertEqual(wrap, RESULTS[task_number])

    def test_wrap_bad(self):
        sizes_list = ad_2.parse_size_file(bad_file)
        self.assertEqual(sizes_list, -1)


if __name__ == '__main__':
    unittest.main()

