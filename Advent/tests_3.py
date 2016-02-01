import unittest
import ad_3


DIRECTIONS_SAMPLES = (
    ('<<<<<<', 7, 4),   # 7 houses for one Santa, 4 houses for two
    ('<><><>', 2, 7),
    ('<^>v<^>v', 4, 3)
)


class TestGeneral(unittest.TestCase):
    def check(self, task_type):
        for sample in DIRECTIONS_SAMPLES:
            del_plan = ad_3.DeliveryPlan(task_type)
            self.assertEqual(del_plan.follow_directions(sample[0]),
                             sample[ad_3.TYPE[task_type]])

    def test_general(self):
        self.check('SILVER')
        self.check('GOLD')


if __name__ == '__main__':
    unittest.main()