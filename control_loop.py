myName= input( "enter your name: ")
print("my name is ",myName)
print(5*5)


num = (int)(input("Enter a number: "))
if num <0:
    print(num, "is negative!")
else:
    print(num, "is positive")
        
num = (int)(input("Enter a number: "))
if num >0:
    print("Num ",num, "is positive!")
else :
    print(num, "is negative")
    
    
#hash is for comment

#this is nested if
x=1
if x:
    y=2
    if y:
        print('block2')
    print('block1')
print('block0')
    
#else 
    
num=(int)(input("enter a number: "))
if num<0:
    print(num,"is negative")
else:
    print(num,"is positive")
    
    
#elif
    
num=(int)(input("enter a number: "))
if num<0:
    print(num,"is negative")
elif num>0:
    print(num,"is positive")
else:
    print(num,"is zero")    
            
    
  
    
num=(int)(input("enter a number: "))
result= (-1 if num<0 else 1)
print(result,"result is ")


#looping 


print("using values from tuple")
for i in(1,3,5,7,9):
    print (i),
    
print()
    
print("now calc the value from the range function")
for i in range(1,10,2):
    print(i),
print()
print("done")



#using for1
num=(int)(input("enter number"))
for i in(1,2,3,4):
    if i>num:
        break
    print(i)
else:
    print("all iterations done")
    
    
    
 #repeat loop
 
fx=0
x=0
while fx<500:
    fx=2*x*(x+1)
    print(x,"\t: ", fx)
    x+=1
print("done")   
    
    
    
    
x=100
x=x+1
print(x)
print(type(x))

x = 0O53
print(x)

x = 0xFF
print(x)

format = "%x"
print(format %x)


#lower case to upper case
x='good'
y='day'
z=x+y
print(z)
print(z.upper())


#list
list1=[]
list2=[4]
list3=[2,4,6]
list4=[1,"two",3,"four"]
list5=[[2,4],[6,8]]
print (type(list5))
print(list1,":",len(list1))
print(list2,":",len(list2))
print(list3,":",len(list3))
print(list4,":",len(list4))
print(list5,":",len(list5))


list1=[2,4,6]
list1.insert(3,7)
print(list1)



#list 2nd chap

list1=[2,4,6,8]
print(list1.index(8))
print(list1.index(3))


#Tuple
tuple=(1,3,5,7)
print(len(tuple))

#range
for i in range(10,1,-2):
    print(i)


#list comprehension 

list1=[1,2,3,4,5]
list2=[el+1 for el in list1] 
print(list2)


first10squares=[x+x for x in range(1,10,1)]
print(first10squares)

#dictionaries
d={"one":1,"two":2}
del d["two"]
print(d)

d={"spring":("mar","apr","may"),"winter":("dec","jan","feb")}
print(d.values())



#none data type
var=100
print(type(var))
var=None
print(type(var))





#casestudy 1
import datetime
month_birth=int(input("enter a month of birth(1-12)"))
day_birth=int(input("enter a day(1-31)"))
year_birth=int(input("enter year of birth(y-y-y-y)"))

current_month = datetime.date.today().month
current_day = datetime.date.today().day
current_year = datetime.date.today().year

num_sec_day=24*60*60
num_sec_year=365*num_sec_day
avg_num_sec_year=((4*num_sec_year)+(num_sec_day)) //4
avg_num_sec_month=(avg_num_sec_year)//12

age_year= current_year - year_birth
age_month= current_month - month_birth
age_day= current_day - day_birth

ageyear_sec= age_year*365*24*60*60
agemonth_sec=age_month*31*24*60*60
ageday_sec=age_day*24*60*60

agesec= ageyear_sec+agemonth_sec+ageday_sec
print(agesec)

#casestudy 2
#deg f to c

tempc=float(input("enter temp in farenheit: "))

faren = (tempc-32)*5/9
print(tempc, "degrees in farenheit is ",format(faren,".1f"), "degree celcius")

#deg c to f
tempc=float(input("enter temp in celc: "))

faren = (tempc*9/5)+32

print(tempc, "degrees in celc is ",format(faren,".1f"), "degree faren")




#3 chap

def hello():
    print("inside a function")
    
hello()




def makealist(start,end):
    newlist=list(range(start,end))
    newlist.insert(0,"[")
    newlist.append("]")
    return newlist
    
print(makealist(5,10))



def dict():
    return{"one":1,"two":2}
print(dict())

xyz=dict
print((xyz())




#named param

def namedparam(**params):
    for p in params.keys():
        print("param",p,"has value",params[p])

namedparam(a=1,b=2,c=3)

def named2(start,end,**namedparams):
    print("positional:",start,end)
    print(namedparams)
    
named2("one","two",thirdArg=3,fourthArg="four")



#passing list and Tuple

def f(*args):
    print("Args:",args)
a=(1,2,3,4,5)
f(0,a,5) 


def f(*args):
    print("Args:",args)
a=[1,2,3,4]
b=[1,2,3,4]
f(0,*a) 






#exception handling 
values=[1,2,3]
try:
    for x in values:
        print( x, values[x])
        
except IndexError as target:
    print("exception:")
    print(target)
    
    
 #2   
    
def f1():
    print("f1 in")
    f2()
    print("f1 out")
    
def f2():
    print("f2 in")
    f3()
    print("f2 out")
    
def f3():
    print("f3 in")
    raise "bang!"
    print("f3 out")
    

try:
    f1()
except Exception as reason:
    print(reason)


#3

values = [1,2,3]
x=5
try:
    y=values[x]
except:
    print("exception:")
    
else:
    print("normal",y)


#4

values = [1,-2,3]

try:
    for x in values:
        if x < 0:
            raise ValueError ("Negative Array Index!!")
        print(x)
except ValueError as value:
    print
    print("exception: "+str(value))




#FILE HANDLING
fileName=r"f:\python\xyz.txt"
f=open(fileName,"r+")
f.write("hellodjfdbbdsb \n")
f.write("fsjkbddvj \n")
f.write("skfd \n")

line1= f.readline()
line2= f.readline()
line3= f.readline()

i=1

for line in f:
    print(i,":", line)
    i=i+1
    
f.close()
print(f.closed)

#2

fileName=r"f:\python\xyz.txt"
f=open(fileName,"r+")
try: 
    for line in f:
        print(line)

finally:
    f.close()
    

#3 seek file

fileName=r"f:\python\xyz1.txt"
f=open(fileName,"r+")
f.write("hello \n")
f.seek(10,0)
f.write("to suven1")
f.seek(0,0)
line1=f.read()
print(line1)




#regular exp
#1

import re 
line1 = "max size is 99.34"
containsIntegers = r"\d+"
rePattern = re.compile(containsIntegers)
matchLine1 = rePattern.search(line1)
if matchLine1:
    print("line1 contains nums")
else:
    print("line1 does not contain nums")
    
    

#2

import re 
drink = "pepsi|limca|sprite"
request = "get me some limca"
if re.search(drink,request):
    print("you must be over 21")
else:
    print("ok then")


#3anchors
         
import re 
line="root: 0:0system admin:/var/root:/bin/sh"
rootUser = r"root:"
if re.search(rootUser,line):
    print("root")
else:
    print("not root")
    
    
#4 wildcards
import re 
name="JohnDoe"
nameRe = r"john" 
if re.search(nameRe, name,re.IGNORECASE):
    print("match")


#5 repeat quantifiers

import re

line="boink, boinkk, boinkkk"
sound= r"boink+"
if re.search(sound, line):
    print("sound exists")
    
else:
    print("doesnt exist")


#6 
import re 
inputstr="888-888 8888"
if re.search(r"\d{3}-\d{2,4}\s\d{4,8}", inputstr):
    print("good job")
else:
    print("not good")

#capture groups


import re 

getComponents = r"(\D+)(\d+)(\D+)(\d+)"
inputText = "abcs123defg456"
matchResults = re.search(getComponents, inputText)
captureGroups = matchResults.groups()
for group in captureGroups:
    print(group)
    
    #split
    
    
    
    import re
p= re.compile(r'\W+')
s="200 Main Street"

print(p.split(s))



import re
pattern=re.compile("(red|green|blue)")
input= "red shirt,yellow shorts  and blue socks"
print(pattern.subn('white',input))