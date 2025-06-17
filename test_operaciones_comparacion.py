import unittest
from operaciones_comparacion import (
    es_mayor_que, es_menor_que, es_mayor_o_igual_que, es_menor_o_igual_que,
    son_iguales
)

class TestOperacionesComparacion(unittest.TestCase):

    def test_es_mayor_que(self):
        self.assertTrue(es_mayor_que(7, 5))
        self.assertFalse(es_mayor_que(5, 8))
        self.assertFalse(es_mayor_que(5, 5))

    def test_es_menor_que(self):
        self.assertTrue(es_menor_que(5, 7))
        self.assertFalse(es_menor_que(5, 4))
        self.assertFalse(es_menor_que(5, 5))

    def test_es_mayor_o_igual_que(self):
        self.assertTrue(es_mayor_o_igual_que(5, 3))
        self.assertTrue(es_mayor_o_igual_que(5, 5))
        self.assertFalse(es_mayor_o_igual_que(3, 5))

    def test_es_menor_o_igual_que(self):
        self.assertTrue(es_menor_o_igual_que(5, 7))
        self.assertTrue(es_menor_o_igual_que(5, 5))
        self.assertFalse(es_menor_o_igual_que(7, 5))

    def test_son_iguales(self):
        self.assertTrue(son_iguales(7, 7))
        self.assertFalse(son_iguales(7, 8))

if __name__ == '__main__':
    unittest.main()
