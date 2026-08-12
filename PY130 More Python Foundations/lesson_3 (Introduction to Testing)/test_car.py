import unittest

class Car:
    def __init__(self):
        self.name = None
        self.wheels = 4

class TestCar(unittest.TestCase):
    def setUp(self):
        self.car = Car()

    def test_wheels(self):
        self.assertEqual(4, self.car.wheels)

    def test_in_collection(self):
        lst = [1, 2, 3]
        lst.append(self.car)
        self.assertIn(self.car, lst)

    def test_name(self):
        self.assertIsNone(self.car.name)

if __name__ == '__main__':
    unittest.main()