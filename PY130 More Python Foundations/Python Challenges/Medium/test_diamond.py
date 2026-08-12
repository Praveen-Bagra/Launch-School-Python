# import unittest
# from diamond import Diamond

# class TestDiamond(unittest.TestCase):
    # def test_display1(self):
        # expected = 'A'
        # self.assertEqual(expected, Diamond('A').display())

    # def test_display12(self):
        # expected = ('  A\n'
                    # ' B B\n'
                    # 'C   C\n'
                    # ' B B\n'
                    # '  A')
        # self.assertEqual(expected, Diamond('C').display())

    # def test_display3(self):
        # expected = ('    A\n'
                    # '   B B\n'
                    # '  C   C\n'
                    # ' D     D\n'
                    # 'E       E\n'
                    # ' D     D\n'
                    # '  C   C\n'
                    # '   B B\n'
                    # '    A')
            
        # self.assertEqual(expected, Diamond('E').display())

# if __name__ == '__main__':
    # unittest.main()

import unittest
from diamond import Diamond

class DiamondTest(unittest.TestCase):

    # @unittest.skip
    def test_letter_a(self):
        answer = Diamond.make_diamond('A')
        self.assertEqual("A\n", answer)

    # @unittest.skip
    def test_letter_b(self):
        answer = Diamond.make_diamond('B')
        expected = " A \nB B\n A \n"
        self.assertEqual(expected, answer)

    # @unittest.skip
    def test_letter_c(self):
        answer = Diamond.make_diamond('C')
        expected = "  A  \n" \
                   " B B \n" \
                   "C   C\n" \
                   " B B \n" \
                   "  A  \n"
        self.assertEqual(expected, answer)

    # @unittest.skip
    def test_letter_e(self):
        answer = Diamond.make_diamond('E')
        expected = "    A    \n" \
                   "   B B   \n" \
                   "  C   C  \n" \
                   " D     D \n" \
                   "E       E\n" \
                   " D     D \n" \
                   "  C   C  \n" \
                   "   B B   \n" \
                   "    A    \n"
        self.assertEqual(expected, answer)

if __name__ == '__main__':
    unittest.main()
