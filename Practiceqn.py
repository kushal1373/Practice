#question no 1
a,b=input("Enter the numbers")
if a==b:
    print("1")
elif a >b:
    print("2")
else:
    print("3")



##qn no 2.
a,b,c,d=input("enter a\n"), input("enter b\n"), input("enter c\n"), input("enter d\n")
if a==b or c==d:
    print("hello")
else:
    print(" more")

##qn no 3.
a=input("Enter a\n")
b=input("Enter b\n")
c=input("Enter c\n")
d=input("Enter d\n")
if a==b and c ==d:
    print("Hello")
else:
    print("once more ")


##Qn no.4
x = float(input("x: "))
if x>0:
    print("True")
elif x==0:
    print("False")
else:
    print("zero")

##Question no.5
num = int(input("Enter a number: "))
if num % 2 ==0:
    print("{}is Even".format(num))
else:
    print("{} is odd\n".format(num))


#Question no 6
marks ={}
total = 0
subjects =[
"MAth",
"Chemistry",
"Physics",
"Psychology"
]

for subject in subjects:
    marks[subject]=input("Enter "+subject +" marks : ")
for key in marks.values():
    total += int(key)
percentage =(total*100)/ 500
if percentage>=70:
    print("Distinction")
elif percentage >=60:
    print("first")
elif percentage>=40:
    print("pass")
else:
    print("You have fail") 


#qn no 7
a="Apple"
b="apple"
c=a==b
print(c)


##question no 8
def personaldetails():
    Name, Age = "kushal", 19
    Address = "Pokhara, kathmandu"
    print("Name: {}\nAge: {}\nAddress: {}".format(Name, Age, Address))

personaldetails()

###question no 9.
from math import pi
r=float(input("Enter radius of circle : "))
print("Area of the circle is: " +str(pi*r**2))

### question no 10.
SectionA=int(input("Enter total number of students in sec A"))
SectionB=int(input("Enter total number of students in sec B"))
SectionC=int(input("Enter total number of students in sec C"))
desk1=SectionA/2
desk2=SectionB/2
desk3=SectionC/3
Totaldesk=desk1+desk2+desk3
print(f"the total number of desk required to fill the students is {Totaldesk}\n")


#### qn no 11.
Salary=int(input("Enter your salary"))
if Salary<2000:
    tax=15/100*Salary
    print(f"your tax is {tax}")
elif Salary<2000 and Salary<50000:
    tax=25/100*Salary
    print(f"yout tax is{tax}")
elif Salary>=50000 and Salary<=100000:
    tax=30/100*Salary
    print(f"your tax is {tax}")
elif Salary>=100000:
    tax=35/100*Salary
    print(f"your tax is {Salary}")
else:
    print("sorry we cannot proceed")


###qn no 12
a=int(input('Enter number: '))
b=int(input('Enter number: '))
c=int(input('Enter number: '))
list=[a,b,c]
smallestnumber=min(list)
print(smallestnumber)

#question no 14
list = [1,2,3,45]
print(5 in list)

#question no.15
num=int(input("Enter numbers from 1 to 12: "))
if num==1:
    print("January")
elif num==2:
    print("February")
elif num==3:
    print("March")
elif num==4:
    print("April")
elif num==5:
    print("May")
elif num ==6:
    print("June")
elif num ==7:
    print("July")
elif num ==8:
    print("August")
elif num ==9:
    print("September")
elif num ==10:
    print("October")
elif num ==11:
    print("November")
elif num ==12:
    print("December")
else:
    print("Invalid number")

##qn no.16
x=5
print(x)
x+=3
print(x)

##qn no 18
Aryan =int(input("Enter your age: "))
Sachin=int(input("Enter your age: "))
Junkiri=int(input("Enter your age: "))

if Aryan>Sachin and Aryan>Junkiri:
    print("Aryan is the oldest")
elif Sachin>Aryan and Sachin>Junkiri:
    print("Sachin is the oldest")
else:
    print("Sachin is the oldest")
if Aryan<Sachin and Aryan<Junkiri:
    print("Aryan is the youngest")
elif Sachin<Aryan and Sachin<Junkiri:
    print("Sachin is the youngest")
else:
    print("Junkiri is the youngest")

#Q.No.19
age = int(input("Enter your age:"))
if age >= 18:
    print("You are eligible for voting")
else :
    print("Sorry, you are not eligible for voting \nSo sad")


#Q.No.20
num = int(input("Enter your number:"))
if num % 7==0 :
    print("The number is divisible by 7")
else:
    print("The number is not divisible by 7")

##q.no.21
city = input ("Enter your city name:")
if city == 'Delhi':
    print ("Your monument is: Red Fort ")
elif city == 'Agra':
     print ("Your monument is: Taj Mahal ")
elif city == 'Jaipur':
     print ("Your monument is: Jal Mahal ")
else:
    print("NO cities available")

##qn no 22
number = int(input("Enter your number:"))
if number % 2==0 and number % 3 == 0:
    print("Your number is divisible by both 2 and 3")
else :
    print("Your number is not divisible by 2 and 3")

##qn no 23
a= int(input("Enter first number:"))
b= int(input("Enter second number:"))
print("1.+ , 2.- , 3.* , 4./")
operator = int(input("choose operator :"))

if (operator == 1):
    print ("Addition of {} and {} is {}".format(a,b,a+b))
elif (operator == 2):
    print ("Substraction of {} and {} is {}".format(a,b,a-b))
elif (operator == 3):
    print ("Multiplication of {} and {} is {}".format(a,b,a*b))
elif (operator == 4):
    print ("Division of {} and {} is {}".format(a,b,a/b))
else:
    print("operator error")


##qn no 24
'''
if test expression:
    statement(s)
Here,the program evaluates the test expression and will execute statement(s) only if the test expression is True.

If the test expression is False, the statement(s) is not executed.

In Python, the body of the if statement is indicated by the indentation. The body starts with an indentation and the first unindented line marks the end.

Python interprets non-zero values as True. None and 0 are interpreted as False
'''

##qn no 25
num = int(input("Enter your number:"))
if num % 5 == 0:
    print("Hello")
else:
    print("Bye")

##qn no 26
print("Select number from 1 to 7")
num=int(input("Enter your number:"))
if num == 1:
    print("Sunday")
elif num == 2:
    print("Monday")
elif num == 3:
    print("Tuesday")
elif num == 4:
    print("Wednesday")
elif num == 5:
    print("Thursday")
elif num == 6:
    print("Friday")
elif num == 7:
    print("Saturday")
else:
    print("invalid")

##qn no 27
'''
the logical operator are:
A>B & C>D
'''


##qn no 28
num=int(input("Enter your number:"))
if (num>100 and num<999):
    print("It is three digit number")
else:
    print("It is not three digit number")

##qn no 29
age=float(input("Enter your age:"))
if age >= 60:
    print("You are a senior citizen.")
else :
    print("You are not a senior citizen.")

##qn no 30
num1= int(input("Enter you number:"))
num2= int(input("Enter you number:"))
if num1 > num2:
    print("Num2 is lowest")
else:
    print("num1 is lowest")

#Q.No.31
""" elif is the correct statement in python """

##q.no.32
a = int(input("Enter total number of working days:"))
b = int(input("Enter number of days absent:"))
per = (a-b)/a*100
print ("Your attendence is",per)
if per < 75:
    print("You cannot attend the exam")
else :
    print("You can attend the exam")

##qn no.33
per = float(input("Enter your percentage:"))
if per < 40:
    print("Failed")
elif per >=40 and per < 55 :
    print("Fair")
elif per >=55 and per < 65 :
    print("Good")
elif per >= 65 and per <=100:
    print("Excellent")
else:
    print("loooseeeee")

##qn no 34
Age=int(input("Enter your age:"))
sex=input("Enter your sex(M/F):")
days=int(input("Enter number of days"))
if Age >=18 and Age < 30 and sex.upper()=='M':
    amt = days*700
    print("Total wages is:",amt)
elif Age >=18 and age < 30 and sex.upper() == 'F':
    amt = days*750
    print("Total wages is:",amt)
elif Age >= 30 and age <= 40 and sex.upper() == 'M':
    amt = days*800
    print("Total wages is:",amt)
elif Age >= 30 and age <= 40 and sex.upper() == 'F':
    amt = days*850
    print("Total wages is:",amt)   
else :
    print("Enter appropriate age")

##qn no 35
Num1 = int(input("Enter your number:"))
Num2 = int(input("Enter your number:"))
Num3 = int(input("Enter your number:"))
if Num1 > Num2 and Num2 > Num3:
    print("Number is the second largest number")
elif Num1 > Num3 and Num3 > Num2:
    print("Number2 is the second largesst number")
elif Num3 > Num1 and Num1 > Num2:
    print("Number is the second largest number")
else:
    print("Invalid number")

##qn no 36
days = int(input("Enter the days you have borrowed the book:"))
if days <= 5:
    print("Two rupees per day")
elif days >= 6 and days <=10:
    print("Three rupees per day")
elif days >=11 and days <=15:
    print("Four rupees per day")
elif days > 15:
    print("Five rupees per day")
else :
    print("Invalid Days.")

##qn no 37
a = True
b = True
c = True
d = True
print (c) 
print (d)
print (not a)
print(not b)
print(not c)
print(not d)
print(a and b)
print(a or b)
print(a and b or c)
print(not a or b or c)
print(not a or not b or not c)
print(not(not a or not b or not c))
