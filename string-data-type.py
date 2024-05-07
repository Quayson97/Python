#decalring a variable and output the assigned value 
myString = "This is a string."
print(myString)

#Printing the type of mystring
print(type(myString))

#String concatenation 
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

#Input Strings
name = input("What is your name? ")
print(name)

#Formatting output strings 
color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")
print("{}, you like a {} {}!".format(name,color,animal))
