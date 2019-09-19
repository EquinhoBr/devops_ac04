from unittest import TestCase
from com.erick.operacoes import Operacoes

class TestOperacoes(TestCase):

	def setUp(self):
		self.operacoes = Operacoes()
		
	def test_soma(self):
		self.assertEqual(
			self.operacoes.soma([1,5]), 6, 'A resposta é 6')

	def test_soma(self):
		self.assertEqual(
			self.operacoes.soma([15,10]), 25, 'A resposta é 25')
			
	def test_mult(self):
		self.assertEqual(
			self.operacoes.mult([10,5]), 50, 'A resposta é 50')