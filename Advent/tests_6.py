import unittest
import ad_6


class TestAll(unittest.TestCase):
    def test_edit_and_count_silver(self):
        grid = ad_6.LightGrid('SILVER', (5, 5))
        grid.edit_square(((0, 0), (2, 2)), ad_6.choose_command_silver('on'))
        self.assertEqual(grid.count_lit(), 9)
        grid.edit_square(((1, 1), (3, 3)), ad_6.choose_command_silver('toggle'))
        self.assertEqual(grid.count_lit(), 10)
        grid.edit_square(((1, 2), (3, 3)), ad_6.choose_command_silver('off'))
        self.assertEqual(grid.count_lit(), 6)

    def test_edit_and_count_gold(self):
        grid = ad_6.LightGrid('GOLD', (5, 5))
        grid.edit_square(((0, 0), (2, 2)), ad_6.choose_command_gold('on'))
        self.assertEqual(grid.count_lit(), 9)
        grid.edit_square(((1, 1), (3, 3)), ad_6.choose_command_gold('toggle'))
        self.assertEqual(grid.count_lit(), 27)
        grid.edit_square(((1, 2), (3, 3)), ad_6.choose_command_gold('off'))
        self.assertEqual(grid.count_lit(), 21)

    def test_parse_instruction(self):  # Merge these two tests in one?
        test_strings = ('turn on 660,55 through 986,197',
                        'toggle 322,558 through 977,958',
                        'turn off 240,129 through 703,297')
        parsed_instructions = [ad_6.parse_instruction(string) for string in test_strings]
        self.assertEqual([('on', [660, 55], [986, 197]),
                         ('toggle', [322, 558], [977, 958]),
                         ('off', [240, 129], [703, 297])],
                         parsed_instructions)

    def test_pack_instruction(self):
        pass


if __name__ == '__main__':
    unittest.main()
