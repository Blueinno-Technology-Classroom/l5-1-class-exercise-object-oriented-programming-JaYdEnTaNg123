##################################################
'''
Q1a: 
'''
x=9
y=2
##################################################
'''
Q1b: 
'''
x=18
y=2
##################################################
'''
Q2:
'''

class name:
    def __init__(self, first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

##################################################
'''
Q3:
'''
class name:
    def __init__(self, first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    def normal_order(self):
       
        return self.first_name+' '+self.last_name
    def reverse_order(self):
        return self.last_name+' '+self.first_name
##################################################
'''
Q7:
'''

class BankAccount:
    def __init__(self, name,balance):
        self.name = name
        self.balance = 0
        self.transaction_fee = 2

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit: ${amount},     Latest balance: ${self.balance}")

    def withdraw(self, amount):
        if (self.balance < amount + self.transaction_fee):
            print('not enough $money$')
        return
        self.balance -= amount + self.transaction_fee
        print(f"withdraw: ${amount},    Latest balance: ${self.balance}") 
    
    def transfer(self, account, amount):
        if (self.balance < amount + self.transaction_fee):
            print('not enough $money$')
        return
        self.balance -= amount + self.transaction_fee
        account.deposit(amount)
ben = BankAccount()
ben.deposit(80.00)

hal = BankAccount()
hal.deposit(20.00)

ben.transfer(hal, 20.00)

##################################################
'''
Q5:
'''


##################################################
'''
Q6:
'''


##################################################
'''
Q7:
'''


##################################################
