import unittest
from Triangulo import ladosTriangulo


class TestTriangulo(unittest.TestCase):
    def test_equilatero(self):
        self.assertEqual(ladosTriangulo(3, 3, 3), "Equilátero")
        self.assertEqual(ladosTriangulo("5", "5", "5"), "Equilátero")

    def test_isoceles(self):
        self.assertEqual(ladosTriangulo(5, 5, 3), "Isóceles")
        self.assertEqual(ladosTriangulo(5, 3, 5), "Isóceles")
        self.assertEqual(ladosTriangulo(3, 5, 5), "Isóceles")

    def test_escaleno(self):
        self.assertEqual(ladosTriangulo(3, 4, 5), "Escaleno")
        self.assertEqual(ladosTriangulo("2", "3", "4"), "Escaleno")

    def test_nao_possivel(self):
        # soma de dois lados equals ou menor que o terceiro
        self.assertEqual(ladosTriangulo(1, 2, 3), "Não é possível formar um triangulo")
        self.assertEqual(ladosTriangulo(1, 10, 12), "Não é possível formar um triangulo")

    def test_nao_valido(self):
        # entrada não numérica
        self.assertEqual(ladosTriangulo("a", 2, 3), "Não é válido")
        # lados não-positivos
        self.assertEqual(ladosTriangulo(0, 0, 0), "Não é possível formar um triangulo")
        self.assertEqual(ladosTriangulo(-1, 2, 2), "Não é possível formar um triangulo")


if __name__ == '__main__':
    unittest.main()
