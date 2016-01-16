import unittest
import ad_1


TASKS = {
    'SILVER': 1,
    'GOLD': 2
}

DIRECTIONS_SAMPLES = (
    ('(())())(', 0, -1),         # Location = 0, cellar = -1 (never)
    ('((())())())()', 1, 13),    # Location = 1, cellar = 13 (last)
    (')()()(', 0, 1),            # Location = 0, cellar = 1 (first)
    ('(((()((', 5, -1)           # Location = 5, cellar = -1 (never)
)


class TestDirections(unittest.TestCase):
    def check(self, task_type):
        self.santa = ad_1.Santa(task_type)
        for sample in DIRECTIONS_SAMPLES:
            self.assertEqual(self.santa.follow_directions(sample[0]),
                             sample[TASKS[task_type]])

    def test_directions(self):
        self.check('SILVER')
        self.check('GOLD')


if __name__ == '__main__':
    unittest.main()