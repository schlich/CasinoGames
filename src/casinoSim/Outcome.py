'''
Created on Aug 31, 2017

@author: Tyler
'''

class Outcome:
    '''
    classdocs
    '''


    def __init__(self, name, odds):
        '''
        Constructor
        '''
        self.name = name
        self.odds = odds
        
    def __str__(self):
        return "{name:s} ({odds:d}:1)".format_map(vars(self))
    
    def __repr__(self):
        return "Outcome({name:s},{odds:d})".format_map(vars(self))
    
    def __hash__(self):
        return hash(self.name)
    
    def __eq__(self,other):
        return self.name==other.name
    
    def __ne__(self,other):
        return hash(self.name)!=hash(other.name)
    
    def winAmount(self,amount):
        return amount*self.odds
    
    