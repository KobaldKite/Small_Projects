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


class TestGeneral(unittest.TestCase):
    def check_samples(self, task_type):
        for sample in DIRECTIONS_SAMPLES:
            self.santa = ad_1.Santa(task_type)
            self.assertEqual(self.santa.follow_directions(sample[0]),
                             sample[TASKS[task_type]])

    def test_general(self):
        self.check_samples('SILVER')
        self.check_samples('GOLD')


if __name__ == '__main__':
    unittest.main()