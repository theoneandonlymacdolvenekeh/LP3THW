## Animal is-a object (yes, sort of confusing) at the extra credit 
class Animal(object):
    pass

## ??
class Dog(Animal):
    
    def _init_(self, name):
        ## ??
        self.name = name
        
        
## ??
class Cat(Animal):
    def _init_(self, name):
        ## ??
        self.name = name
        
## ??
class Person(object):
    
    
    def _init_(self, name):
        ## ??
        self.name = name
        
        ## person has-a pet of some kind
        self.pet = None
## ??
class Employee(Person):
    def _init_(self, name, salary):
        super(Employee, self). _init_(name)
        ## ??
        self.salary = salary    
        
## ??
class Fish(object):
    pass

## ??
class Salmon(Fish):
    pass

## ??
class Halibut(Fish):
    pass


## ??
rover = Dog("Rover")

## ??
satan = Cat("Satan")

## ??
mary = Person('Mary')

## ??
mary.pet = satan

## ??
frank = Employee("Framk", 120000)

## ??
frank.pet = rover

## ??
flipper = Fish()

## ??
crouse = Salmon()

## ??
harry  = Halibut()
