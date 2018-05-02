import unittest

class ConverteNumeroRomano:
	def __init__(self, numero_romano):
		self.numero_romano = numero_romano
		self.digito.map = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}

	def converte_para_decimal(self):
		val = 0
		for char in sel.numero_romano:
			val += self.digito.map(char)
		return val

class TestConverNumeroRomano(unittest.TestCase):
	def test_mil(self):
		value = ConverteNumeroRomano('M')
		self.assertEqual(1000, value.converte_para_decimal())

	def test_cem(self):
		value = ConverteNumeroRomano('C')
		self.assertEqual(100, value.converte_para_decimal())

	def test_ciquenta(self):
		value = ConverteNumeroRomano('L')
		self.assertEqual(50, value.converte_para_decimal())

	def test_vazio():
		value = ConverteNumeroRomano('')
		self.assertTrue(value.converte_para_decimal() == 0)
		self.assertFalse(value.converte_para_decimal() > 0)

if __name__ == '__main__':
	unittest.main()