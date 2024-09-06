import unittest
from src.questao2 import conta_a 

class TestContaA(unittest.TestCase):
    
    def test_conta_a_present(self):
        exists, qnt = conta_a("Abacaxi")
        self.assertTrue(exists)
        self.assertEqual(qnt, 3)
    
    def test_conta_a_absent(self):
        exists, qnt = conta_a("Teste")
        self.assertFalse(exists)
        self.assertEqual(qnt, 0)
    
    def test_conta_a_mixed_case(self):
        exists, qnt = conta_a("Banana")
        self.assertTrue(exists)
        self.assertEqual(qnt, 3)
    
    def test_conta_a_empty(self):
        exists, qnt = conta_a("")
        self.assertFalse(exists)
        self.assertEqual(qnt, 0)
    
    def test_conta_a_no_a(self):
        exists, qnt = conta_a("xyz")
        self.assertFalse(exists)
        self.assertEqual(qnt, 0)

if __name__ == "__main__":
    unittest.main()
