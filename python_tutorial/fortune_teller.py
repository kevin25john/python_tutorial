import random
have_questions='y'
while have_questions=='y':
    question = input("what is yyour ques: ")
    print("you asked - ",question)
    random_number= random.randint(1,9)
    if random_number==1:
        print("probabilities ae good")
    elif random_number==2:
        print("you already know us")
    elif random_number == 3:
        print("the outlook is dim")
    elif random_number == 4:
        print("you are the only one")
    elif random_number == 5:
        print("yes, successful")
    elif random_number == 6:
        print("no,cant be done")
    elif random_number == 7:
        print("kgjyjfyyf")
    elif random_number == 8:
        print("hvhhh")
    elif random_number == 9:
        print("jchdhdhkdyf")
    have_questions=input("do you want to continue y/n?")
    
print("done")