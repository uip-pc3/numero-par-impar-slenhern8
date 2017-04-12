import unittest
from app.main import par_impar

class Testpar(unittest.TestCase):
    def test_par_impar(self):
        self.assertEquals(par_impar(5),False)
        self.assertEquals(par_impar(4),True)

if __name__ == '__main__':
    unittest.main()
