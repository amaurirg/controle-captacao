from django.test import TestCase


class Soma(TestCase):
    def test_soma(self):
        a = 1
        b = 2
        self.assertEqual(a + b, 3)
