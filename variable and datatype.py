#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      raopr
#
# Created:     04-05-2024
# Copyright:   (c) raopr 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Variable ------------------------------ A variable is a name given to a memory location in a program.

print(23)
print(23+34)

#example : name="Prateek"  here var is name and its value is Prateek, age=23, price=23.45

name = "Prateek"
age = 23
price = 25.43
print(type(name))
print(type(age))
print(type(price))

# type here to represent which datatype of value is

# Datatype : int, str, float, boolean.
    # Int : 24
    # str : "hello"
    # float : 25.4
    # boolean : True / False

name1 = "sk"
name2 = 'sk'
name3 = '''sk'''
print(name1)
print(name2)
print(name3)
#----------------------------
age = 23
old = False
new = True
print(type(old))
print(type(new))

#---------------------------------------

# Keywords : false, true, and none . We use all keywords for their own use .

    # Print Sum

a = 2
b = 3
sum = a+b
print(sum)

#-------------------Define variable

a = 20000
b = 380
subs = a-b
print(subs)

#-----------------------------------

# Types of Tokens

# Punctuators : they are symbols to organize sentencce structure in programming

# Expression Execution : String and Numeric, String and String

# String and Numeric
A,B = 2,4
Txt = "@"
print(2*Txt*4)


A,B = 2,3
Txt = "@"
print(2*Txt*3)

# String and String, it is also know as concatenation
A, B = "Prateek", 3
Txt="@"
print((A +Txt)*B)

A, B = "3", 3
Txt="@"
print((A +Txt)*B)

# Numeric value operation

A,B = 2,3
C = 4
print(A+B*C)

# Arithmetic Expression with integer
A,B =1.2, 5.2
C=A*B
print(C)

# Result of division operator

A,B =1,2
C=A/B
print(C)

#Integer division with float and int
a,b =1.2,2
c=a//b
print(c)


a,b =2.2,2
c=a//b
print(c)

# floor gives closest integer
a,b =12,5
c=a//b
print(c)

a,b =-12,5
c=a//b
print(c)

#remainder is negative when denominator is negative, here in module when ever denominator will be negative or nominator will be positive then remainder will be negative


a,b =-5,2
c=a%b
print(c)

a,b =5,-2
c=a%b
print(c)


# comments in python

#print("hello")

# Input in Python

# string input
    # name = input("name : ")
# int input
    # age = int(input("age : ")
# float input
    # price = float(input("pricee :"))

name = input("name :")
print(name)

age = int(input("age :"))
print(age)

price = float(input("price :"))
print(price)
print("My name is", name, "and I am", age, "year old")


#--------------Conditional Statements------------

    # if-elif-else
    # if(condition):
        # Statement1
    # elif(condition):
        # Statement2
    # else:
        # StatementN

light = input("light : ")
if(light == "red"):
    print("stop")
elif(light == "yellow"):
    print("look")
elif(light == "green"):
    print("go")
else:
    print("light is broken")


#------------------------------------------------

marks = input("marks : ")
if marks >= 90:
    print("A")
elif marks >= 80 and marks < 90:
    print("B")
elif marks >= 70 and marks < 80:
    print("C")
else:
    print("D")



