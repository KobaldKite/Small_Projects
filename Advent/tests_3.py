import os
import unittest
import ad_3


DIRECTIONS_SAMPLES = (
    ('<<<<<<', 7, 4),      # 7 houses for one Santa, 4 houses for two
    ('<><><>', 2, 7),
    ('<>ab<>cd<>', 2, 7),  # Incorrect instructions are ignored
    ('<^>v<^>v', 4, 3),
    ('qwerty', 1, 1)       # Only one delivery: the house Santa starts in
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
        for sample_number, directions_sample in enumerate(DIRECTIONS_SAMPLES):
            temp_file_name = TEMP_FILE_NAMES[sample_number]
            with open(temp_file_name, 'w') as temp_file:
                temp_file.write(directions_sample[0])

    def tearDown(self):
        clear()

    def check(self, task_type):
        for sample_number, directions_sample in enumerate(DIRECTIONS_SAMPLES):
            del_plan = ad_3.DeliveryPlan(task_type)
            self.assertEqual(del_plan.do_the_job(TEMP_FILE_NAMES[sample_number]),
                             directions_sample[ad_3.TYPE[task_type]])

    def test_general(self):
        self.check('SILVER')
        self.check('GOLD')


if __name__ == '__main__':
    unittest.main()