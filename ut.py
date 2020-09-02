import unittest
from Calculator import Calc

class CalculatorTest(unittest.TestCase):
    Calculator = Calc()
    
    def test_add(self):
        assert 4 == Calc.add(2, 2)
        #self.assertEqual(4, Calculator.add(2,2))
        #self.assertEqual(3.2, Calculator.add(1,2.2))

    def test_minus(self):
        assert 2 == Calc.minus(3, 1)
        '''self.assertEqual(2, Calculator.minus(3,1))
        self.assertEqual(-2, Calculator.minus(1,3))'''

    def test_multiple(self):
        assert 12 == Calc.multiple(3, 4)
        '''self.assertEqual(12, Calculator.multiple(3,4))
        self.assertEqual(16, Calculator.multiple(4,4))'''

    def test_devide(self):
        assert 3 == Calc.devide(9, 3)
        '''self.assertEqual(3, Calculator.devide(9,3))'''

if __name__ == "__main__":
    unittest.main()
