import unittest
import sourse
 
class CalcTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(sourse.add(1, 2), 3)
        
    def test_sub(self):
        self.assertEqual(sourse.sub(4, 2), 2)
        
    def test_mul(self):
        self.assertEqual(sourse.mul(2, 5), 10)
        
    def test_div(self):
        self.assertEqual(sourse.div(8, 4), 2)
        
if __name__ == '__main__':
    unittest.main()