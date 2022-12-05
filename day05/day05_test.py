import unittest
from day05 import day05


class TestStringMethods(unittest.TestCase):

    def test_parse_instructions(self):
        [_count, _from, _to] = day05.parse_instruction("move 22 from 7 to 5")
        self.assertEqual(_count, 22)
        self.assertEqual(_from, 7)
        self.assertEqual(_to, 5)

    def test_parse_drawing(self):
        parsed = day05.parse_drawing('''    [D]    
[N] [C]    
[Z] [M] [P]''')
        print(parsed)


if __name__ == '__main__':
    unittest.main()
