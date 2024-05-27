#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      raopr
#
# Created:     30-04-2024
# Copyright:   (c) raopr 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------
print("hello world")
print("hello coders!")
print("I know how to count .. 1 2 3 4 5 6 ..")
print("Hello world")
#here we use double cotation which represent to print msg
#and also we can't capital P to print any msg
print("Prateek")
# If we want to store any data here that is variable, ex: variable name :

name = "Prateek"
age = 22
print(name)
print(age)
name = "Noman"
print(name)

# here if i want to change the variable value then it will print the new value


name = "Prateek"
age = 24.0
is_adult = True
print(name)
print(age)

age = 17
is_adult = False
print(age)
print(name)
print("name")

# whenever we are going to store boolean value first we have to give value then
#then we have to give statement like true or false



# question1. Add a person with a name Tony Stark. Tony's age is 51 years old. Tony is a genius.

# here we will take input from user before we print input to screen

name = input("what is your name?")
print(name)
#concatenation
# here i will going to print name with one message with use of concatenation

print("hello"  +  name)

# changing age with old to new one
# here we can concatenate string with string
# here old_age is a string format where i changed it into int format to make it concatenation
# we can convert it into this float(), str(), boolean()
# we can concatenate float with float, string with string, int with int, etc.

old_age = input("enter your old age:")

int(old_age)

new_age = int(old_age) + 2

print(new_age)

new_age = input("enter your new age")
int(new_age)
old_age = int(new_age) -1
print(old_age)

number = 18
print(float(18))


first = input("enter first number :")
second = input("enter second number :")
sum = (first) + (second)
sum = int(first) + int(second)
print (sum)