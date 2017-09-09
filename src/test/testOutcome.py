'''
Created on Aug 31, 2017

@author: Tyler
'''
import unittest
from casinoSim.Outcome import Outcome


class TestOutcome(unittest.TestCase):
    def setUp(self):
        self.firstRed = Outcome('Red',1)
        self.secondRed = Outcome('Red',1)
        self.street123 = Outcome('Street 1-2-3',11)

    def testEqual(self):
        self.assertEqual(self.firstRed,self.secondRed,'Objects are equal')
        
    def testNotEqual(self):
        self.assertNotEqual(self.firstRed, self.street123, 'Objects are not equal')
    
    def testString(self):
        self.assertEqual(str(self.firstRed), 'Red (1:1)', 'string is a match')
        
    def testWinAmount(self):
        self.assertEqual(self.street123.winAmount(3),33, 'win amount is correct')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()