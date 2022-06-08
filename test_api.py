import unittest
import API_Area

class TestApiArea(unittest.TestCase):

    def test_validate(self):
        self.assertTrue(API_Area.validate([1, 2, 3, 4, 5]))
        self.assertFalse(API_Area.validate([1]))
        self.assertTrue(API_Area.validate([1, 2, 3, 105]))
        self.assertFalse(API_Area.validate([1, 2, 106, 4, 5, 6]))
        self.assertFalse(API_Area.validate([1, 0, 3, 105]))
    
    def test_maxArea(self):
        self.assertEqual(API_Area.maxArea([1, 2, 3, 4, 5]), 6)
        self.assertEqual(API_Area.maxArea([1,8,6,2,5,4,8,3,7]), 49)
        self.assertNotEqual(API_Area.maxArea([13, 64, 83, 49, 27]), 90)
        self.assertEqual(API_Area.maxArea([13, 64, 83, 49, 27]), 98)
        self.assertNotEqual(API_Area.maxArea([13, 64, 83, 49, 27]), 0)

def main():
    unittest.main()

if __name__ == "__main__":
    main()
