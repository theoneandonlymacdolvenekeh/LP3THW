class other(object):
    
    def override(self):
        print("OTHER override()")
        
    def implicit(self):
        print("OTHER implicit()")
        
    def altered(self):
        print("OTHER altered()")
        
class Child (object):
    def _init_(self):
        self.other = other()
        
    def implicit(self):
        self.other.implicit()
    
    def override(self):
        print("CHILD override()")
        
    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD, AFTHER altered()")
        
son = Child()
son.implicit()
son.override()
son.altered()