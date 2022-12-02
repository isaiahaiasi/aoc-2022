import unittest
from day02 import day02

'''
calling from CLI:
python -m unittest test_module1 test_module2
python -m unittest test_module.TestClass
python -m unittest test_module.TestClass.test_method
'''

LOSE = 0
TIE = 3
WIN = 6


class TestStringMethods(unittest.TestCase):

    def test_get_result_score(self):
        self.assertEqual(day02.get_result_score(1, 1), TIE)
        self.assertEqual(day02.get_result_score(1, 2), WIN)
        self.assertEqual(day02.get_result_score(1, 3), LOSE)
        self.assertEqual(day02.get_result_score(2, 1), LOSE)
        self.assertEqual(day02.get_result_score(2, 2), TIE)
        self.assertEqual(day02.get_result_score(2, 3), WIN)
        self.assertEqual(day02.get_result_score(3, 1), WIN)
        self.assertEqual(day02.get_result_score(3, 2), LOSE)
        self.assertEqual(day02.get_result_score(3, 3), TIE)

    def test_get_hand_score(self):
        self.assertEqual(day02.get_hand_score(1, 0), 3)
        self.assertEqual(day02.get_hand_score(1, 1), 1)
        self.assertEqual(day02.get_hand_score(1, 2), 2)
        self.assertEqual(day02.get_hand_score(2, 0), 1)
        self.assertEqual(day02.get_hand_score(2, 1), 2)
        self.assertEqual(day02.get_hand_score(2, 2), 3)
        self.assertEqual(day02.get_hand_score(3, 0), 2)
        self.assertEqual(day02.get_hand_score(3, 1), 3)
        self.assertEqual(day02.get_hand_score(3, 2), 1)


if __name__ == '__main__':
    unittest.main()
