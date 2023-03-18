# Encapsulation is a fundamental concept of object-oriented programming (OOP) that allows objects 
# to keep their internal state hidden from the outside world, and to control access to their data and behavior.
# In Python, encapsulation can be achieved through the use of access modifiers, such as public, private, and protected.


class BankAccount:
    def __init__(self, account_number, balance,name):
        self.__account_number = account_number # private attribute
        self.__balance = balance # private attribute
        self.name = name
    
    def get_account_number(self):
        return self.__account_number
    
    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds")
        else:
            self.__balance -= amount

# create an instance of BankAccount
my_account = BankAccount("1234567890", 1000,'zainul')

# try to access private attributes directly
# print(my_account.__account_number) # Error: AttributeError
# print(my_account.__balance) # Error: AttributeError
print(my_account.name)


# access private attributes using public methods
print(my_account.get_account_number()) # "1234567890"
print(my_account.get_balance()) # 1000

# try to modify private attributes directly
my_account.__balance = 2000 # does not modify the balance attribute
print(my_account.get_balance()) # 1000

# modify private attributes using public methods
my_account.deposit(500)
print(my_account.get_balance()) # 1500

my_account.withdraw(2000) # "Insufficient funds"
my_account.withdraw(500)
print(my_account.get_balance()) # 1000
