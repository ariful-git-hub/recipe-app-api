

from django.test import SimpleTestCase

from app import calc


class CalcTest(SimpleTestCase):
     
    def test_add(self):
        result = calc.add(5,10)
        
        self.assertEqual(result,15)
        
    def test_subtract(self):
        result = calc.subtract(15,10)
        
        self.assertEqual(result,5)