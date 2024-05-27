print("helloworld")
print("helloworld\nhelloworld")
print("hello" + "Prateek")
print("Hello" + "" + input("what is your name"))
print("Hey" + "" + input("What is your name?") + "," + input ("How are you?"))
name=input("What is your name?")
length=len(name)
print(length)
a=1
b="Prateek"
print(a)
print(b)

a=input("enter value of a")
b=input("enter value of b")
temp = a
a = b
b = temp
print("a=" + a)
print("b=" + b)

name = "Prateek"
age = 30
name = "Rao"
age = 34
print(name)
print(age)

old_age=input("enter your age")
new_age = int(old_age)+2
print(new_age)

number = 20
print(float(20))


first = input("enter first number :")
second = input("enter second number :")
sum = float(first) + float(second)
print(sum)


first = input("enter first number :")
second = input("enter second number :")
sum = int(first) + int(second)
print(sum)

var_1 = 121
var_2= 13.4
print(var_1 + var_2)
print(type(var_1))
print(type(var_2))

var_1 = 0o123
print(var_1)
print(type(var_1))

name = "Prateek"
print(name[3])

name_1 = "123"
name_2 = "456"
print(name_1 + name_2)

name_1="Prateek"
name_2="456"
print(name_1 + name_2)


name_1="Prateek"
name_2="Rao"
print(name_1 + name_2)

print("PRateek\'s \"Lectures\"")
print("PRateek\'s\n \"Lectures\"")
print("PRateek\'s\\n \"Lectures\"")

var_1=True
print(var_1)
print(type(var_1))

a=1
b=2
var=a<b
print(var)
print(type(var))

a=1
b=2
var=a>b
print(var)
print(type(var))

print(len("Prateek"))
length=len("Prateek")
print("Your name has" +str(length) + " characters")
new_length=str(length)
print(type(new_length))
print(type(length))

print(int("10") + int("20"))
print(int("10") + float("20"))
name=123
print(10 + int(name))
first_number = input("enter fiest number:")
second_number = input("enter second number:")

sum=int(first_number) + int(second_number)
print(sum)

name = "Prateek"
print(name.lower())
print(name)
name = "Prateek"
print(name.find('t'))
print(name.find('P'))
print(name.find('k'))
name = "Prateek"
print(name.find('K'))
print(name.replace("Prateek","Hero"))
print(name)
print("p" in  name)
print("P" in  name)

print(5/2)
print(5//2)
print(5%2)
print(5**2)
print(5+2)
print(5-2)
print(5+2*8//2/3+3%6)

print(3==3)
print(3!=3)
print(2>3 or 2>1)
print(not 2>3)


age=13
if age >=18:
    print("you are an adult")
    print("you can vote")
elif age < 18 and age >3:
    print("you are in school")
else:
    print("you are child")
print("thankyou")

#-------------------------------------------------


first = input("enter first number :")
operator = input("enter operator (+,-,*,/,%) :")
second = input("enter second number :")

first =int(first)
second=int(second)
if operator=="+":
    print(first + second)
elif operator=="-":
    print(first - second)
elif operator=="*":
    print(first * second)
elif operator=="/":
    print(first / second)
elif operator=="%":
    print(first % second)
else:
    print("invalid operator")

i=1
while i<=5:
    print(i)
    i = i + 1

    i = 1
    while i <= 5:
        print(i * "*")
        i = i + 1

    i = 5
    while i >= 0:
        print(i * "*")
        i = i - 1

for item in range(5):
    print(item +2)


marks = [95, 98,87,88,89,90,91,92]
for score in marks:
    print(score)

print(marks[-5])
print(marks[5])
print(marks[4:8])
print(marks[0:8])
marks=[90,91,92]
marks.insert(0,88)
print(marks)
print(len(marks))

students=["Prateek", "Piyush", "Ashish", "Cipriyan"]
for student in students:
    if student == "Ashish":
        break
    print(student)
for student in students:
    if student == "Ashish":
        continue
    print(student)

marks = (95, 85, 70, 75, 85, 85)

print(marks.count(85))
print(marks.index(85))

marks = {95, 85, 70, 75, 85, 85}

for score in marks:
    print(score)



marks={"english":97, "chemistry":98}
print(marks["english"])
marks={"english":97, "chemistry":98}
print(marks["english"])
marks["physics"]= 95
print(marks)
marks["physics"]=100
print(marks)



import math
print(dir(math))
from math import sqrt
print(sqrt(16))

def print_sum(first, second):
    print(first + second)

print_sum(1, 2)