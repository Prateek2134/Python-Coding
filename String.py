#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      raopr
#
# Created:     30-04-2024
# Copyright:   (c) raopr 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# String
#Upper and lower case
name = "Prateek Rao"
print(name.upper())
print(name)
print(name.lower())
print(name)

#finding char in string
name = "Prateek Rao"
print(name.find('r'))
print(name.find('e'))
print(name.find('Rao'))

#if we will going to print with change in case upper or lower and also use alphabet which are not in a string it will give you -1
name = "Prateek Rao"
print(name.find('T'))
print(name.find('z'))

name = "Prateek Rao"
print(name.replace("Prateek", "Chanty"))
print(name.replace("Prateek Rao", "Chanty"))

name = "Prateek"
print(name.replace("P", "R"))
print(name)


#variable will highlated with blue color
#printing alphabet and string in input or not
name = "Prateek Rao"
print('P' in name)
print('M' in name)
print("Prateek" in name)
print("Chanty" in name)

#-------Dictionary-----------------

info = {
    "key" : "value",
    "name" : "Prateek",
    "learning" : "coding"
}

print(info)

