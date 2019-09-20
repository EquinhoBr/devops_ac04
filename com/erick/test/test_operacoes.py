from unittest import TestCase
from com.erick.multiplica import Multi

class TestMultiplicacao(TestCase):

	def setUp(self):
		self.multiplica = Multi()
			
	def test_mult(self):
		self.assertEqual(
			self.multiplica.mult([10,5]), 50, 'A resposta é 50')