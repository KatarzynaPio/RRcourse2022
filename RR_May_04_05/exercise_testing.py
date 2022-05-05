import unittest 
import sys 

def convert(f, target = 'c'):
    
    if target == 'c': 
        return (f - 32) / 1.8
    
    elif target == 'k':
        return ( (f - 32) / 1.8) + 273.15
    else:
        return Exception('wrong target')
    
    
    
class TestDivide(unittest.TestCase):
    def test_convert(self):
        self.assertAlmostEqual(convert(50, 'c'), 10)
        self.assertAlmostEqual(convert(70, 'c'), 21.1111111)
        self.assertAlmostEqual(convert(90, 'c'), 32.2222222)

if __name__  == '__main__':
    unittest.main()