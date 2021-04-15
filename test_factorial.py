import unittest
import factorial


class TestFactorial(unittest.TestCase):

    def test_fact(self):
        self.assertEqual(factorial.factorial(1), 1)

    def test_fact2(self):
        self.assertEqual(factorial.factorial(4), 24)

    def test_fact3(self):
        self.assertEqual(factorial.factorial(6), 720)

    def test_fact4(self):
        self.assertEqual(factorial.factorial(5), 120)

    def test_fact5(self):
        self.assertEqual(factorial.factorial(10), 3628800)


if __name__ == '__main__':
    unittest.main()
