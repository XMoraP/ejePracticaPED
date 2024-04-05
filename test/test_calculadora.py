import unittest
from aplicacion.calculadora import CalculadoraDescuento
calculadora = CalculadoraDescuento()

class Test(unittest.TestCase):
	def testDescuentoPorcentaje(self):
		precioYDescuento = [100, 10]
		resultado = calculadora.calcularPorcentaje(precioYDescuento)
		self.assertEqual(90, resultado)

if __name__ == '__main__':
	unittest.main()
