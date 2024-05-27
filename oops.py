#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      raopr
#
# Created:     01-05-2024
# Copyright:   (c) raopr 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# class:A class is a collection of objects. A class contains the blueprints or the prototype from which the objects are being created.
# the class is a blue print of an object.

class car:
    def __init__(self,modelname, year):
        self.modelname = modelname
        self.year = year
    def display(self):
        print(self.modelname,self.year)

c1 = car("Toyota", 2016)
c2 = car("BMW", 2019)
c1.display()
c2.display()
#-------------------------------------------------------------------------------
# Objects:
    #State: It is represented by the attributes of an object. It also reflects the properties of an object.
    #Behavior: It is represented by the methods of an object. It also reflects the response of an object to other objects.
    #Identity: It gives a unique name to an object and enables one object to interact with other objects.


class car:
    def __init__(self,modelname, year):
        self.modelname = modelname
        self.year = year
    def display(self):
        print(self.modelname,self.year)

c1 = car("Toyota", 2016)
c2 = car("BMW", 2019)
c1.display()
c2.display()

# Method--------------------------------------
class Calculator:
    def add(self, a, b):
        return a + b

# Create an instance of the Calculator class
calc = Calculator()

# Call the add method
result = calc.add(3, 5)
print("Result of addition:", result)


#Inheritant-----------------------------------------

# Parent class
class Animal:
    def sound(self):
        print("Animal makes a sound")

# Child class inheriting from Animal
class Dog(Animal):
    def sound(self):
        print("Dog barks")

# Create an instance of Dog
dog = Dog()

# Call the sound method of Dog
dog.sound()

#polymorphism-----------------------
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

# Function that takes an Animal object and calls its sound method
def make_sound(animal):
    animal.sound()

# Create instances of Dog and Cat
dog = Dog()
cat = Cat()

# Call make_sound function with different objects
make_sound(dog)
make_sound(cat)

# Class and Objects---------**********************
# creating class
class Student:
    name = "Prateek Rao"
    age = "21"
print(Student.name)
print(Student.age)


# creating object(instance)

s1 = Student()
print(s1.name)
print(s1.age)




#------------------------
class Student:
    name1 = "Prateek Rao"
    age1 = "21"
    name2 = "Chanty Rao"
    age2 = "22"



# creating object(instance)

s1 = Student()
print(s1.name1)
print(s1.age1)

s2 = Student()
print(s2.name2)
print(s2.age2)


#----------------------


class Car:
    color = "blue"  # Use '=' for assignment instead of ':'
    brand = "BMW"

car1 = Car()
print(car1.color)  # Access attributes using '.' notation
print(car1.brand)


#-----Constructor or init function: it is used to invoke, when ever we will declare object constructor will be executed .

# car1 = Car()-> constructor


class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

# Creating an instance of the Car class
car1 = Car("blue", "BMW")

# Accessing instance variables
print("Car 1 - Color:", car1.color)
print("Car 1 - Brand:", car1.brand)

#------------------------------------

class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

# Creating an instance of the Car class
car1 = Car("blue", "BMW")

# Accessing instance variables
print(car1.color)
print(car1.brand)


# Class and Instance Attributes : every class or instance or we can say every student should have their own attributes or values.May be it should be specific.
class Student:
    college_name = "CMR College"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("Adding new student in Database..")

# Creating the first student object
s1 = Student("Prateek", 98)
print(s1.name, s1.marks)

# Creating the second student object (corrected the missing comma)
s2 = Student("Rahul", 88)
print(s2.name, s2.marks)


#-----Static method: method that don't use the self parameter work at class level.

class Student:
    @staticmethod
    def college():
        print("college")

# Call the static method directly on the class
Student.college()



# Abstraction and Encapsulation : Hiding the implementation detail of a class and only showing the essential features to the user.

# Encapsulation : data + method wrapping data and functions into a single unit (object).


class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("Car started..")

car1 = Car()
car1.start()


