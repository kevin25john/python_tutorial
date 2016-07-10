#inheritense

class Account:
    def __init__(self,balance):
        self.balance = balance
    def deposit(self,amount):
        self.balance +=amount
    def withdraw (self,amount):
        self.balance -=amount
    def getbalance(self):
        return self.balance

    def printme(self):
        print("Account",self.__class__,self.balance)
        
class ChequeAccount(Account):
    def __init__(self,balance,overdraft):
        Account.__init__(self, balance)
        self.overdraft = overdraft
        
    def printme(self):
        print("chequeAccount",self.__class__,self.balance,self.overdraft)
        
class SavingsAccount(Account):
    def __init__(self,balance,interest):
        Account.__init__(self, balance)
        self.interest = interest 
        
a=Account(100)
c=ChequeAccount(200,50)
s=SavingsAccount(300,5)

a.printme()
c.printme()
s.printme()        