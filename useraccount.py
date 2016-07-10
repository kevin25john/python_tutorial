import bank.account
a1=bank.account.Account(0)

a2=bank.account.Account(300)
a1.deposit(100)
a1.withdraw(40)
a2.deposit(200)
print("bal is ",a1.getbalance())
print("bal is ",a2.getbalance())
