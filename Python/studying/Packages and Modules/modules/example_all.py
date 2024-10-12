import unittest

# all() function take iterable element and return True if all elements is True

list_which_return_false = [True, False, True]
list_which_return_true = [True, True, True]


class TestFunction(unittest.TestCase):
    def test_false(self):
        self.assertFalse(all(list_which_return_false))

    def test_true(self):
        self.assertTrue(all(list_which_return_true))


if __name__ == "__main__":
    unittest.main()
