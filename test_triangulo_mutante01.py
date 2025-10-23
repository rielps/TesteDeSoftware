import unittest
from Triangulo import ladosTriangulo

class TestTriangulo(unittest.TestCase):
    def test_equilatero(self):
        self.assertEqual(ladosTriangulo(3, 3, 3), "Equilátero")
        self.assertEqual(ladosTriangulo("5", "5", "5"), "Equilátero")
        

if __name__ == '__main__':
    unittest.main()
