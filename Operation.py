#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      raopr
#
# Created:     01-05-2024
# Copyright:   (c) raopr 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Operators
# Arithmetics
print(5+2)
print(5-2)
print(5*2)
print(5/2)
print(8/2)
# here we use // to remove right side number or after decimal number
print(5//2)
# here we use ** 2 for square ** 3 for cube
print(3**2)
print(7**3)
print(2**4)

# Rules

#i = 5
#i = i+2 / i += 2
#i = i-2 / i -= 2
#i = i*2 / i *= 2

# Operator Precidence
result = 2+3*5
print(result)
result = (2+3)*5
print(result)

# Comments ---------------------------


# Assignment Operators

print(3<2)
print(3>2)
print(3==2)
print(3==3)
print(3>=2)
print(3>=3)
print(3!=2)


#logical operator
# Or operator (if 1 is true out of both ans is true)
print(2>1) or (2>3)
# and operator (if both the condition is true it will give true other wise false)
print(2>1) and print(3>2)
print(2>3) and print(3>2)
# not operatorwill used to make true to false, false to true
print(not 2>3)
print(not 3>1)
# If else
age = 15
if age >= 18:
    print("you are adult")
elif age < 18 and age >3:
    print("you are in school")
else:
    print("you are a kid")

#---------------------------------
age = 27
if age >= 18:
    print("you are adult")
elif age < 18 and age >3:
    print("you are in school")
else:
    print("you are a kid")
#---------------------------------
age = 1
if age >= 18:
    print("you are adult")
elif age < 18 and age >3:
    print("you are in school")
else:
    print("you are a kid")

# lets build a calculator

first = input("enter first numer :")
operator =input("enter operator (+,-,*,/,%):")
second = input("enter second numbed :")

first = int(first)
second = int(second)

if operator == "+":
    print(first + second)
elif operator == "-":
    print(first - second)
elif operator == "*":
    print(first * second)
elif operator == "/":
    print(first / second)
elif operator == "%":
    print(first % second)
else:
    print("invalid")
