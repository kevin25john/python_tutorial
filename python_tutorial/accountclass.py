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