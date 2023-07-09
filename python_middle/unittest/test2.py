import unittest

def add(x, y):
    return x + y

class TestAdd(unittest.TestCase):
    def test_true(self):
        self.assertTrue(add(1, 2)== 3)
        self.assertTrue(add(2, 3)== 5)
        self.assertTrue(add(3, 4)== 7)
        
    
    def test_false(self):
        self.assertFalse(add(-1, 2) == 3)
        self.assertFalse(add(1, -2) == 3)
        self.assertFalse(add(11, 12) == 3)

if __name__ == '__main__':
    unittest.main()
