from unittest import TestCase
from com.erick.operacoes import Operacoes

class TestOperacoes(TestCase):

	def setUp(self):
		self.operacoes = Operacoes()
			
	def test_mult(self):
		self.assertEqual(
			self.operacoes.mult([10,5]), 50, 'A resposta é 50')