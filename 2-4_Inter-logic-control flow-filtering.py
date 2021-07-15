# LOGIC, CONTROL FLOW AND FILTERING

# Boolean logic is the foundation of decision-making in Python programs.

# Comparison operators
# Comparison operators are operators that can tell how two Python values relate, and result in a boolean.
import numpy as np
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
bmi = np_weight / np_height ** 2
bmi
# Using comparison operator to find out which values > 23
bmi > 23
# Use the resulting boolean to select the value
bmi[bmi > 23]
# Numeric comparators
2 < 3    # smaller than
2 == 3   # equal to
2 <= 3   # smaller or equal to
# String comprisons
"car" == "train"
"car" < "train"  # "car" comes before "train" aphabetically 
3 < "car" # error because integers can't be compared with strings.
# Equality
2 == (1 + 1)
"Python" != "python"  # not equal to
True != False
True == 1  # True, by default True has value of 1 and False has value of 0.
# Greater and less than
True > False
x = -3 * 6
print(x >= -10)
y = "test"
print("test" <= y)
# Compare arrays
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])
print(my_house >= 18)
print(my_house < your_house)

# Boolean operators
# "and" operator
True and True
True and False
False and True
False and False
x = 12
x > 5 and x < 15 # True and True
# "or" operator
True or True
True or False
False or True
False or False
y = 5
y < 7 or y > 13 # True or False
# "not" operator
not True
not False
# Combine boolean opeartors
my_kitchen = 18.0
your_kitchen = 14.0
print(my_kitchen > 10 and my_kitchen < 18)
print(my_kitchen < 14 or my_kitchen > 17)
print(2 * my_kitchen < 3 * your_kitchen)
# Boolean operators with Numpy
bmi > 21 and bmi < 22  # does not work in Numpy.
# Use boolean functions from the Numpy package
np.logical_and(bmi > 21, bmi < 22)
# Create two Numpy arrays
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])
print(np.logical_or(my_house > 18.5, my_house < 10))
print(np.logical_and(my_house < 11, your_house < 11))

# Conditional statements
# if condition
z = 4
if z % 2 == 0 : 
    print("z is even")
# If the condition does not pass, the expression is not executed
z = 5
if z % 2 == 0 :
    print("checking " + str(z))
    print("z is even")  # no output
# else statement
if z % 2 == 0 :
    print("z is even")
else :
    print("z is odd")
# elif customises even more behaviour
z = 3
if z % 2 == 0 :
    print("z is divisible by 2")
elif z % 3 == 0 : 
    print("z is divisible by 3")
else :
    print("z is neither divisible by 2 nor 3")
# Experiment with if, elif and else
area = 10.0
if area < 9.0 :
    print("small")
elif area < 12 :
    print("medium")
else :
    print("large")
# Define variables for your house
room = "kit"
area = 14.0
if room == "kit" :
    print("looking around in the kitchen.")
elif room == "bed" :
    print("looking around in the bedroom.")
else : 
    print("looking around elsewhere.") 
if area > 15 :
    print("big place!")
elif area > 10 :
    print("medium size, nice!")
else : 
    print("pretty small.")

# Filtering pandas DataFrames
# Import csv file
import pandas as pd
import numpy as np
brics = pd.read_csv("0_data/brics.csv", index_col = 0)
brics
# Select countries with over area greater than 8 million square kilometers
brics["area"]   # get column
# Alternatives
brics.loc[:, "area"]
brics.iloc[:, 2]
# Compare
is_huge = brics["area"] > 8 # return a series containing Boolean
# Subset DataFrame
brics[is_huge]
# Write one-liner code
brics[brics["area"] > 8]
# Add Boolean operators
np.logical_and(brics["area"] > 8, brics["area"] < 10) # create a Boolean series
# Subset DataFrame
brics[np.logical_and(brics["area"] > 8, brics["area"] < 10)]
# Import cars data
cars = pd.read_csv("0_data/cars.csv", index_col = 0)
# Extract drives_right column
dr = cars["drives_right"] 
sel = cars[dr]
print(sel)
# Convert to one-liner code
sel = cars[cars["drives_right"]]
print(sel)
# Select the cars_per_cap column from cars
cpc = cars["cars_per_cap"]
# Filter observations that have a cars_per_cap over 500
many_cars = cpc > 500
# Subset 
car_maniac = cars[many_cars]
print(car_maniac)
# Filter observations with cars_per_cap between 100 and 500
between = np.logical_and(cpc > 100, cpc < 500)
medium = cars[between]
print(medium)