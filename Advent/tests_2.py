import unittest
import ad_2


SIZES_SAMPLES = (
    (10, 10, 6),    # 500 paper, 632 ribbon
    (-10, 10, 6),   # Negative dimension, the box is ignored
    (10, 10, 10)    # 700 paper, 1040 ribbon
)

RESULTS = (1200, 1672)


class TestGeneral(unittest.TestCase):  # TODO: add smaller tests!
    def test_wrap(self):
        for task_number, task_type in enumerate(ad_2.TYPE):
            self.assertEqual(ad_2.wrap_boxes(SIZES_SAMPLES, task_type), RESULTS[task_number])


if __name__ == '__main__':
    unittest.main()

