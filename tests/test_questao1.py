import unittest
from src.questao1 import fibonacci 

class TestFibonacci(unittest.TestCase):
    
    def test_fibonacci_positive(self):
        self.assertTrue(fibonacci(0))
        self.assertTrue(fibonacci(1))
        self.assertTrue(fibonacci(2))
        self.assertTrue(fibonacci(3))
        self.assertTrue(fibonacci(5))
        self.assertTrue(fibonacci(8))
        self.assertTrue(fibonacci(13))
        self.assertTrue(fibonacci(21))
    
    def test_fibonacci_negative(self):
        self.assertFalse(fibonacci(-1))
        self.assertFalse(fibonacci(-10))
    
    def test_fibonacci_not_in_sequence(self):
        self.assertFalse(fibonacci(4))
        self.assertFalse(fibonacci(6))
        self.assertFalse(fibonacci(7))
        self.assertFalse(fibonacci(9))
        self.assertFalse(fibonacci(10))
    
    def test_fibonacci_large_number(self):
        
        # Exemplo de número grande na sequência de Fibonacci
        self.assertTrue(fibonacci(832040))  
        
        # Número grande que não está na sequência
        self.assertFalse(fibonacci(832041)) 

if __name__ == "__main__":
    unittest.main()
