#Account (defining and using a class

class Account:
    def __init__(self,balance):
        self.balance = balance
    def deposit(self,amount):
        self.balance +=amount
    def withdraw (self,amount):
        self.balance -=amount
    def getbalance(self):
        return self.balance

a1 = Account(0)
a2 = Account(400)
a1.deposit(100)
a1.withdraw(40)
a2.deposit(400)
print("balance is ",a1.getbalance())
print("balance is", a2.getbalance())


#2


class exampleClass:
    eyes="black"
    age="30"
    
    def thismethod(self):
        return"entering method"
    
exampleobject= exampleClass()
print(exampleobject.eyes)



#3



class Account:
    def __init__(self,balance):
        self.balance = balance
    def deposit(self,amount):
        self.balance +=amount
    def withdraw (self,amount):
        self.balance -=amount
    def getbalance(self):
        return self.balance

a3=Account(0)
a4=a3
a4.deposit(100)
print("a3 bal is",a3.getbalance())


#4 obj id

class Account:
    def __init__(self,balance):
        self.balance = balance
    def deposit(self,amount):
        self.balance +=amount
    def withdraw (self,amount):
        self.balance -=amount
    def getbalance(self):
        return self.balance

a3=Account(0)
a4=a3
a4.deposit(100)
print("a3 bal is",a3.getbalance())
print("a3 id is",id(a3))
print("a4 id is",id(a4))


#5 class data

class account:
    numaccount = 0
    def __init__(self,balance):
        self.balance = balance
        account.numaccount +=1
        
    def howManyAccounts(self):
        return account.numaccount;

a1=account(0)
a2=account(300)
print("we have created",a1.howManyAccounts(),"accounts")
print("we have creates",a2.howManyAccounts(),"accounts")



#case study 7

import sys

while True:
    try:
        x=int(input("enter an integer: "))
        r = 1/x
        break
    except:
        print("oops!",sys.exc_info()[0],"occured")
        print("plz try again bitch!")
        print()
        
print("the reciprocal of ",x,"is",r)




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