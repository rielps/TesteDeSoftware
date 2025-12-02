import unittest
import FizzBuzz


class TesteFizzBuzz(unittest.TestCase):
    def testNormal(self):
        self.assertEqual(1, FizzBuzz.FizzBuzz(1))
     
if __name__ == '__main__':
     unittest.main()

