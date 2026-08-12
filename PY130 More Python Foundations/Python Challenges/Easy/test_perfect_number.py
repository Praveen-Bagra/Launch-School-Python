# import unittest
# from perfect_number import NaturalNumber

# class TestNaturalNumber(unittest.TestCase):
    # def test_invalid_number(self):
        # with self.assertRaises(TypeError):
            # NaturalNumber('13')

    # def test_invalid_number2(self):
        # with self.assertRaises(TypeError):
            # NaturalNumber('hello')

    # def test_invalid_number3(self):
        # with self.assertRaises(ValueError):
            # NaturalNumber(-12)

    # def test_invalid_number3(self):
        # with self.assertRaises(ValueError):
            # NaturalNumber(0)

    # def test_perfect_category(self):
        # self.assertEqual('Perfect', NaturalNumber(1).category())

    # def test_perfect_category2(self):
        # self.assertEqual('Perfect', NaturalNumber(6).category())

    # def test_perfect_category3(self):
        # self.assertEqual('Perfect', NaturalNumber(28).category())

    # def test_deficient_category(self):
        # self.assertEqual('Deficient', NaturalNumber(15).category())

    # def test_deficient_category2(self):
        # self.assertEqual('Deficient', NaturalNumber(7).category())

    # def test_deficient_category3(self):
        # self.assertEqual('Deficient', NaturalNumber(13).category())

    # def test_abundant_category(self):
        # self.assertEqual('Abundant', NaturalNumber(24).category())

    # def test_abundant_category(self):
        # self.assertEqual('Abundant', NaturalNumber(12).category())
        
import unittest
from perfect_number import PerfectNumber

class PerfectNumberTest(unittest.TestCase):
    # @unittest.skip
    def test_initialize_perfect_number(self):
        try:
            PerfectNumber.classify(-1)
            self.fail("Expected exception not raised")
        except ValueError as e:
            self.assertEqual(str(e), "Input must be a positive integer")

    # @unittest.skip
    def test_classify_deficient(self):
        result = PerfectNumber.classify(13)
        self.assertEqual(result, "deficient")

    # @unittest.skip
    def test_classify_perfect(self):
        result = PerfectNumber.classify(28)
        self.assertEqual(result, "perfect")

    # @unittest.skip
    def test_classify_abundant(self):
        result = PerfectNumber.classify(12)
        self.assertEqual(result, "abundant")

if __name__ == "__main__":
    unittest.main()
