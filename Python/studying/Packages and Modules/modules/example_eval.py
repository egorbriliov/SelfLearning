import unittest


# eval() function parses and executes a string expression as Python code

class TestFunction(unittest.TestCase):
    def test_1(self):
        expression = "1 + 2"
        self.assertEqual(eval(expression), 3)

    def test_2(self):
        a, b = 1, 2
        expression = "a + b"
        self.assertEqual(eval(expression), 3)


if __name__ == "__main__":
    unittest.main()
