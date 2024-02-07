import unittest

#наследуемся от класса TestCase
class TestAbs(unittest.TestCase):
    #self-ссылка на экземпляр класса
    def test_abs1(self):
        self.assertEqual(abs(-42), 42, "Should be absolute value of a number")
        
    def test_abs2(self):
        self.assertEqual(abs(-42), -42, "Should be absolute value of a number")
        
if __name__ == "__main__":
    unittest.main()