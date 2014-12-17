import unittest

def add_one(number):
    return number + 1

class TestAddOne(unittest.TestCase):
    def test_add_one_returns_number_plus_one(self):
        assert add_one(1) == 2

if __name__ == "__main__":
    unittest.main()
