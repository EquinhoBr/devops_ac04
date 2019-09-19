from unittest import TestCase
from com.erick.operacoes import Operacoes

class TestOperacoes(TestCase):

	def setUp(self):
		self.operacoes = Operacoes()
		
	def test_soma(self):
		self.assertEqual(
			self.operacoes.soma([1,5]), 6, 'O correto seria 6')

	def test_soma(self):
		self.assertEqual(
			self.operacoes.soma([15,10]), 25, 'O correto seria 25')