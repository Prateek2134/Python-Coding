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
# Function: it consist of different operation
# each part consist of some operation
#type: 1. In-Build Fn's 2. Module Fn's 3. User Defined Fn's

# in-build:
# int()
# Str()
# bool()


# module:

# import math-print(dir(math))
from math import sqrt
print(sqrt(4))
print(sqrt(16))

# user defined Function:- def function_name(parameter):
# first define function and name of fn's then parameter taking i/p adn giving o/p

def print_sum(first, second):
    print(first + second)

print_sum(1, 2)

#----------------------------
def print_sum(first, second=4):
    print(first + second)

print_sum(1)



#------------function------------------

    # func_name(arg1, arg2, ...) #function call (argument)


def my_function():
  print("Hello from a function")

my_function()


#-------------------------------------

def greet():
    print("hello")
    print("good morning")


greet()
greet()
greet()
greet()
greet()

#--------------------------------------


def add(x,y):
    c = x+y
    return c

result = add(5,4)
print(result)

#-------------------------------------


def div(x,y):
    c = x/y
    return c

result = div(5,4)
print(result)

#---------------------------------------

def add_sub (x,y):
    c = x+y
    d = x-y
    return c,d
result1, result2 = add_sub(5,4)
print(result1, result2)


#-------------------------------------------

def factorial(n):
    if n == 0:  # Base case: factorial of 0 is 1
        return 1
    else:
        return n * factorial(n - 1)  # Recursive call to factorial function

# Example usage:
number = 5
print("Factorial of", number, "is", factorial(number))
