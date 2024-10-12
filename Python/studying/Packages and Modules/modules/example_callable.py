import unittest


# callable() function take object and return True if it can be called

def function_to_call():
    return None


variable_to_call = None


class TestFunction(unittest.TestCase):
    def test_false(self):
        self.assertFalse(callable(variable_to_call))

    def test_true(self):
        self.assertTrue(callable(function_to_call))


if __name__ == "__main__":
    unittest.main()
