from datetime import datetime
zodiac_animal = ("rat","ox","tiger","rabbit","dragon","snake","horse","goat","monkey","rooster","dog","pig")

rat= "forthright, industries"
ox="dependable, methodical"
tiger="unpredictable,aggressive"
rabbit="good friend,kind"
dragon="strong,self assured"
snake="deep thinker,creative"
horse= "cheerful,quick witted"
goat= "soncere,symphatatic"
monkey="motivator, kind"
rooster= "organised, self assured"
dog = "honest,easy going"
pig="peaceful,trusting"

characteristics=(rat,ox,tiger,rabbit,dragon,snake,horse,goat,monkey,rooster,dog,pig)
terminate= False
print("this is a prog will dispay chinese zodiac callender")
current_year=datetime.now().year
while not terminate:
    birth_year= int(input("enter your birth year in YYYY: \n"))
    while birth_year<1900 or birth_year>current_year:
        print("invalid year,please re enter \n")
        
        birth_year=int(input("enter your birth year in YYYY: \n"))
    
    cycle_num=(birth_year-1900)%12
    
    print("your chinese zodiac sign is the ", zodiac_animal[cycle_num],'\n')
    print("your personal characteristics...")
    print(characteristics[cycle_num])
    
    response= print("would you like to enter another year ? y/n")
    
    while response!= "y" and response !="n":
        response=input("plz enter y or n : ")
        
    if response=='n':
        print("thankyou :D")
        terminate=True
    