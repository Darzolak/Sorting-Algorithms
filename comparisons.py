"A module to assist with tracking various algorithmic operations."

import hashlib, traceback, sys

class Counter(object):
    "A counter can be used to keep track of the number of operations."
    
    def __init__(self):
        self.reset()
    
    def increment(self):
        "Increment the count."
        
        if not self.locked:
            self.count += 1
    
    def comparison(self, expression):
        self.increment()
        
        return expression
    
    def lock(self):
        self.locked = True
    
    def reset(self):
        "Reset the count to zero."
        
        self.count = 0
        self.locked = False
    
    def __repr__(self):
        return repr(self.count)

def digest(structure):
    return hashlib.sha224(str(structure).encode('utf-8')).hexdigest()
