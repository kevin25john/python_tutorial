#casestudy4
#tax=0.15
#amunt of gift certi = input 


tax=0.15
print("this prog will calc resturant bill")
amt_certificate= float(input("enter gift certi: "))
print("enter certi per person")

appetizer_per1=float(input("appetizer1: "))
drink_per1=float(input("drink1: "))
food_per1=float(input("food1:" ))

appetizer_per2=float(input("appetizer2: "))
drink_per2=float(input("drink2: "))
food_per2=float(input("food2:" ))

amt_per1=appetizer_per1+drink_per1+food_per1
amt_per2=appetizer_per2+drink_per2+food_per2

item_count=(amt_per1+amt_per2)*0.15

total_amt = item_count - amt_certificate

print("the total bill is : ", total_amt)