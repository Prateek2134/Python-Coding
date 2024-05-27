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
#Range
numbers = range(5) # 0,1,2,3,4
print(numbers)

#loop
print(1)
print(2)
print(3)
print(4)
print(5)

#loop is a concept which used to manage in a single time

#while
i = 1
while i <= 5:
    print(i)
    i = i + 1

#straight
i = 1
while i<= 5:
    print(i * "*")
    i = i+1


i = 1
while i<= 5:
    print(i *"hello")
    i = i+1

# reverse
i = 5
while i>= 0:
    print(i * "*")
    i = i-1


#for

for i in range(5):
    print(i)
#-------------------------
for i in range(5):
    print(i+1)

#list

marks = [95, 98, 97]
print(marks)

print(marks[0])
print(marks[1])
print(marks[2])
print(marks[-1])
print(marks[-2])
print(marks[-3])
# we cant define -4 because it will be out of range

print(marks[0:2])
print(marks[0:3])
print(marks[1:3])
print(marks[0:1])
print(marks[1:2])
print(marks[2:3])

#use for on list
marks = [95, 96, 97]
for score in marks:
    print(score)

#append operation
marks =[95, 97, 98]
marks.append(99)
print(marks)

#insert operaion
marks =[95, 97, 98]
marks.insert(0,99) # here 0 is a index value of new marks value 99
print(marks)

print(99 in marks)
print(93 in marks)

#lenth
marks = [98,99,100]
print(len(marks))

# while on list

i = 0
while i < len(marks):
    print(marks[i])
    i = i+1
# clear
marks.clear()
print(marks)

# break using for anf if
students = ["ram", "shyam", "raj", "sai", "raju"]

for student in students:
    if student == "sai":
        break;
    print(student)
#------------------
# continue
for student in students:
    if student == "sai":
        continue;
    print(student)


#---------------------------------------------
# tuples we define it has ()
marks =(95,98,97,97,97)
print(marks.count(97))
print(marks.count(95))
print(marks.index(97))


#-----------------------------------------------
#sets: it is used to stores unique number. Also a grp of number
# it is represented by {}
# Note: list : [], tuple : (), sets : {}
marks ={95,98,97,97,97}
print(marks)
# it will not recognised index value of every value
# it is unorder

marks ={95,98,97,97,97}


for score in marks:
    print(score)
# Dictionary: we will stores with key value. It is a pair of key and value

marks = {"english" : 95, "chemistry" : 89}

print(marks["chemistry"])

marks["physics"] = 97;
print(marks)

marks["physics"] = 99;
print(marks)