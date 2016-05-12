import unittest
import run_password_validation


class TestGeneral(unittest.TestCase):
    def setUp(self):
        pass

    def test_no_upper(self):
        self.assertFalse(run_password_validation.validate('asdfg%%%123'))

    def test_no_lower(self):
        self.assertFalse(run_password_validation.validate('ASDFG%%%123'))

    def test_no_digit(self):
        self.assertFalse(run_password_validation.validate('asdFG%%%JJJ'))

    def test_no_symbol(self):
        self.assertFalse(run_password_validation.validate('asdFGJJJ123'))

    def test_too_short(self):
        self.assertFalse(run_password_validation.validate('asD%%23'))

    def test_several_problems(self):
        self.assertFalse(run_password_validation.validate('asdASDasd'))

    def test_good_password(self):
        self.assertTrue(run_password_validation.validate('asdFG%%%123'))

    def test_good_password_exact_length(self):
        self.assertTrue(run_password_validation.validate('asdFG%12'))
