# test_utils.py
# Author: Sébastien Combéfis
# Version: February 8, 2018

import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_fact(self):
        self.assertEqual(utils.fact(5),120)
        with self.assertRaises(ValueError):
            utils.fact(-2)
       


    def test_roots(self):
        self.assertEqual(utils.roots(2,3,4), (-2.9999999999999996+5.5677643628300215j,-3.0000000000000004-5.5677643628300215j))


       
   
    # def test_integrate(self):
    #    # À compléter...
    #    pass

if __name__ == '__main__':
   suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
   runner = unittest.TextTestRunner()
   exit(not runner.run(suite).wasSuccessful())
