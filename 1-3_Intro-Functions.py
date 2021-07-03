# FUNCTIONS

# A function is a piece of reusable code, aimed at solving a particular task. 
# Suppose you have the list of your family members' height:
fam = [1.73, 1.68, 1.71, 1.89]
print(fam)
# Use the max() function to get the maximum value in this list
tallest = max(fam)
print(tallest)

# Built-in functions
# max() is one of the built-in functions, just like type(). 
# round() function that allows you to round up a number.
round(1.68, 1)
# round() takes two inputs: the number you want to round, and the precision. 
# When there is no specific input for precision, the function rounds up the number to its default setting, which results to the closest integer .
round(1.68)
# To understand why both approaches work, open the documentation for round() with another built-in function: help()
help(round)

# Familiar functions
# Python offers a bunch of built-in functions like print(), type(), str(), int(), bool() and float() to switch between data types. 
var1 = [1, 2, 3, 4]
var2 = True
# Use print() in combination with type() to print out the type of var1:
print(type(var1))
# Use len() to get the length of the list var1. 
print(len(var1))
# Use int() to convert var2 to an integer
out2 = int(var2)
type(out2)

# Multiple arguments 
# Suppose you have some lists of numbers and want to sort them out in a descending order:
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]
full = first + second 
# Python provides the sorted() function to perform this task.
help(sorted)
# sorted() takes three arguments: iterable, key and reverse. 
full_sorted = sorted(full, reverse = True)
print(full_sorted)

# Methods
# Python is an object oriented programming language, which means almost everything in Python is an object, with its properties and methods. 
# Methods are basic functions that belong to the objects, depending on which type the object has.
# Use the method .index to get the index of an element in a list: 
fam = ["liz", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89]
fam.index("mom")
# .count method counts the number of times a value occurs in the list
fam.count(1.73) # only Liz is this tall.
# Different objects have specific methods that associated with them. 
# .capitalize method returns a string with the first letter is capitalized.
sister = "liz"
sister.capitalize()
# .replace method replaces some parts of the string with some other parts.
sister.replace("z", "sa")
# A string object has the .replace method, but a list object does not.
fam.replace("mom", "mommy")
# Objects of different types can have methods with the same names.
sister.index("z") # get the index of the letter in the string.
fam.index("mom") # get the index of the element in the list.
# .append method adds elements into the list.
fam.append("me")
fam.append(1.68)
print(fam)

# String methods
# Strings come with a bunch of methods. Discover more detail with help().
help(str)
# Create a string to experiment with:
place = "poolhouse"
# Use the upper() method to capitalize all the letters in the string.
place.upper()
# Count the number of letter "o"s in the string with the count() method.
place.count("o")

# List methods
# Most list methods will change the list they're called on.
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
# append(): adds an element to the list. 
areas.append(24.5)
areas.append(15.45)
print(areas)
# reverse(): reverses the order of the elements in the list.
areas.reverse()
print(areas) 
# remove(): removes the first element of a list that matches the input. 
areas.remove(11.25)  
print(areas)
