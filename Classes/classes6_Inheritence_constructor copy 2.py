class Person:
    def __init__(self, name, job=None, pay=0):
        print("Person init is bing called.")
        self.name = name
        self.job = job
        self.pay = pay

    
    def lastName(self):
        return self.name.split()[-1]
    
    def giveRaise(self,percent):
        self.pay = int(self.pay * (1+percent) )
    

    def __repr__(self):
        return '[Person: %s, %s]' % (self.name, self.pay)


class Manager(Person):
    def __init__(self,name, job='mgr',pay=0):
        print("Manager init is bing called.")
        Person.__init__(self, name, 'mgr', pay)
        
    def giveRaise(self, percent, bonus=.10):
        self.pay = int(self.pay * (1 + percent + bonus)) # Bad: cut and past       

    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self,percent+bonus) 

if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job= 'dev', pay = 100000)

    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())

    tom = Manager('Tom Hiddle', job = 'Manager', pay = 20000)
    print('--All three--')
    for obj in (bob, sue, tom): # Process objects generically
        obj.giveRaise(.10) # Run this object's giveRaise
        print(obj) # Run the common __repr__
