# WRITE YOUR OWN FUNCTIONS

# User-defined functions 
# Built-in functions in Python
str(5) # return a string
# Assign the call to str() as variable to store its return value
x = str(5)
type(x)
# Define a function
def square():           # function header
    new_value = 4 ** 2  # function body
    print(new_value)    
# Now whenever the new function is called, the code in the function is run
square()
# Function parameters
def square(value):         # write parameters in function header
    new_value = value ** 2
    print(new_value)
square(4) # pass the arguments in the function
square(5)
# Return values from functions
def square(value):
    new_value = value ** 2
    return new_value
num = square(4)
print(num)
# Docstrings: describes what your function does
def square(value):
    """Return a square of a value."""
    new_value = value ** 2
    return new_value
# Operations + and * with strings
object1 = "data" + "analysis" + "visualization"
object2 = 1 * 3
object3 = "1" * 3
print(object1)
print(object2)
print(object3)
# Check the data type of the objects
x = 4.89
y1 = str(x)
y2 = print(x)
type(x)
type(y1)
type(y2) # NoneType as y2 only prints but does not return a value.

# Write a simple function
def shout():
    """Print a string with three exclamation marks"""
    # concatenate the strings: shout_word
    shout_word = "congratulations" + "!!!"
    # print shout_word
    print(shout_word)
# Call shout
shout()
# Single parameter function
def shout(word):
    """Print a string with three exclamation marks"""
    shout_word = word + "!!!"
    print(shout_word)
shout("congratulations")
# Functions that return single values
def shout(word):
    """Return a string with three exclamation marks"""
    shout_word = word + "!!!"
    return(shout_word)
yell = shout("congratulations")
yell

# Multiple parameters and return values
# Multiple function parameters
def raise_to_power(value1, value2):
    """Raise value1 to the power of value2."""
    new_value = value1 ** value2
    return new_value
# The order in which the arguments are passed correspond to the parameters
result = raise_to_power(2, 3)
print(result)

# Make functions return multiple values with tuples
# Tuples are like lists which can contain multiple values, but are immutable
even_nums = (2, 4, 6)
type(even_nums)
# Unpacking tuples into several variables
a, b, c = even_nums
print(a)
print(b)
print(c)
# Accessing tuple elements like with list
even_nums[1]
# Returning multiple values
def raise_both(value1, value2):
    """Raise value1 to the power of value2 and vice versa."""
    new_value1 = value1 ** value2
    new_value2 = value2 ** value1
    new_tuple = (new_value1, new_value2)
    return new_tuple
result = raise_both(2, 3)
print(result)
# Define shout with parameters word1 and word2
def shout(word1, word2):
    """Concentrate strings with exclamation marks"""
    shout1 = word1 + "!!!"
    shout2 = word2 + "!!!"
    new_shout = shout1 + shout2
    return new_shout
# Pass "congratulations" and "you" to shout
yell = shout("congratulations", "you")
print(yell)
# Use tuple so that the funtion returns multiple values
def shout_all(word1, word2):
    shout1 = word1 + "!!!"
    shout2 = word2 + "!!!"
    shout_words = (shout1, shout2)
    return shout_words
# Pass 'congratulations' and 'you' to shout_all()
yell1, yell2 = shout_all("congratulations", "you")
print(yell1)
print(yell2)

# Import pandas and the tweets dataset
import pandas as pd
tweets = pd.read_csv("0_data/tweets.csv")
tweets.columns
# Initialize an empty dictionary
langs_count = {}
# Extract column from DataFrame
col = tweets["lang"]
# Iterate over lang column in DataFrame
for entry in col :
    # if the language is in langs_count, add 1 
    if entry in langs_count.keys():
        langs_count[entry] += 1
    # else add the language to langs_count, set the value to 1
    else:
        langs_count[entry] = 1
# Print the populated dictionary
print(langs_count)
# Define a function to count the entries in the DataFrame
def count_entries(df, col_name):
    """Return a dictionary with counts of occurrences as value for each key."""
    langs_count = {}
    col = df[col_name]
    for entry in col:
        if entry in langs_count.keys():
            langs_count[entry] += 1
        else:
            langs_count[entry] = 1
    return langs_count
# Call count_entries() on tweets
result = count_entries(tweets, "lang")
print(result)