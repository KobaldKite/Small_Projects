import unittest
import ad_6


class TestCount(unittest.TestCase):
    def check_count(self, coordinates, command, result):
        self.grid.edit_square(coordinates, self.grid.choose_command(command))
        self.assertEqual(self.grid.count_lit(), result)

    def test_edit_and_count_silver(self):
        self.grid = ad_6.LightGrid('SILVER', (5, 5))
        self.check_count(((0, 0), (2, 2)), 'on', 9)
        self.check_count(((1, 1), (3, 3)), 'toggle', 10)
        self.check_count(((1, 2), (3, 3)), 'off', 6)

    def test_edit_and_count_gold(self):
        self.grid = ad_6.LightGrid('GOLD', (5, 5))
        self.check_count(((0, 0), (2, 2)), 'on', 9)
        self.check_count(((1, 1), (3, 3)), 'toggle', 27)
        self.check_count(((1, 2), (3, 3)), 'off', 21)


class TestParse(unittest.TestCase):
    def test_parse_instruction(self):  # Merge these two tests in one?
        test_strings = ('turn on 660,55 through 986,197',
                        'toggle 322,558 through 977,958',
                        'turn off 240,129 through 703,297')
        parsed_instructions = [ad_6.parse_instruction(string) for string in test_strings]
        self.assertEqual([('on', [660, 55], [986, 197]),
                         ('toggle', [322, 558], [977, 958]),
                         ('off', [240, 129], [703, 297])],
                         parsed_instructions)


if __name__ == '__main__':
    unittest.main()
