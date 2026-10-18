import unittest

def check_password(password):
    if len(password) < 8:
        raise ValueError("Password is too short")
    return True

class TestCheckPassword(unittest.TestCase):
    def test_check_password(self):
        with self.assertRaises(ValueError):
            check_password(password="234")
    def test_long_password_fail(self):
        self.assertTrue(check_password(password="12345678"))