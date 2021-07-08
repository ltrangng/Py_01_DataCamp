# LOOPS

# While loops
# The while loop is similar to an if-statement: it executes the code inside if the condition is True.
# It will continue to execute the code over and over again as long as the condition is True.
error = 50
while error > 1 :
    error = error / 4  # if there is no update to the condition, the while loop will run forever!
    print(error)
# Basic while loops
x = 1
while x < 4 :
    print(x)
    x = x + 1 
offset = 8
while offset != 0 :
    print("correcting...")
    offset = offset - 1
    print(offset)
# Add conditionals
offset = -6
while offset != 0 :
    print("correcting...")
    if offset > 0 :
        offset = offset - 1
    else :
        offset = offset + 1
    print(offset)

# For loops
# For loops can be read as "for each variable in a sequence, execute the expression"
# Create a list for the height of each family's member
fam = [1.73, 1.68, 1.71, 1.89]
print(fam)
# Suppose you want to print each element in the list
print(fam[1])
print(fam[2])
print(fam[3])
print(fam[4]) # tedious and time-consuming!
# Use a for loop instead
for height in fam :
    print(height)
# enumerate() iterates and gives access to the index of each element in the list
for index, height in enumerate(fam) :
    print("index " + str(index) + ": " + str(height))
# Loop over a list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
for room in areas :
    print(room)
# Update loop
for index, a in enumerate(areas) :
    print("room " + str(index) + ": " + str(a))
# Room 0 sounds strange. Adapt the index
for index, a in enumerate(areas) :
    print("room " + str(index + 1) + ": " + str(a))
# Loop over list of lists
house = [["hallway", 11.25], 
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]
for index, x in enumerate(house) :
    print("the " + house[index][0] + " is" + str(house[index][1]) + " sqm")
# Loop over string
for c in "family" :
    print(c.capitalize())

# Loop data structures
# Loop over a dictionary
world = {"afghanistan":30.55, 
         "albania":2.77, 
         "algeria":39.21}
# Call the method .items() for the dictionary in a loop
for key, value in world.items() :
    print(key + " -- " + str(value)) # the printout is unordered.
# Dictionaries in dictionary
europe = { "spain":"madrid", "france":"paris", "germany":"berlin", "norway":"oslo" }
# Iterate over each pair of key:value
for x, y in europe.items() :
    print("the capital of " + x + "is " + y)
# Loop over a 2D Numpy array
import numpy as np
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
meas = np.array([np_height, np_weight])
# Try to print out each element in the 2D array seperately
for var in meas :
    print(var)  # the 2D array is built up from an array of 1D arrays
# Use nditer() from Numpy to get every element of an array
for var in np.nditer(meas) :
    print(var)
# Import the height of the baseball players in inches
from numpy import genfromtxt
np_height = np.array(genfromtxt("0_data/height_in.csv", dtype = "int", delimiter=','))
# For loop over np_height
for x in np_height :
    print(str(x) + " inches")
# Import the 2D array of baseball players' measurement
np_baseball = np.array(genfromtxt("0_data/baseball_2d.csv", dtype = "int", delimiter = ","))
# For loop over np_baseball
for x in np.nditer(np_baseball) :
    print(x)

# Loop over a DataFrame
# Import the csv file containing the brics country data
import pandas as pd
brics = pd.read_csv("0_data/brics.csv", index_col = 0)
# Try to loop over brics
for var in brics :
    print(var) # simply returns column names.
# In Pandas, you have to explicitly mention that you want to iterate over the rows
for lab, row in brics.iterrows() :
    print(lab)  # row label
    print(row)  # row data
# Suppose you only want to print out the capital of each iteration
for lab, row in brics.iterrows() :
    print(lab + ": " + row["capital"])
# Add a new column to the brics DataFrame containing the number of characters in the country's name
for lab, row in brics.iterrows() :
    brics.loc[lab, "name_length"] = len(row["country"])
print(brics)
# Alternatively use appply() instead of loops
brics["name_length"] = brics["country"].apply(len)
print(brics)

# Import the cars csv file
cars = pd.read_csv("0_data/cars.csv", index_col = 0)
# Iterate over rows of cars
for lab, row in cars.iterrows() :
    print(lab)
    print(row)
# Adapt the for loop
for lab, row in cars.iterrows() :
    print(lab + ": " + str(row["cars_per_cap"]))
# Add column
for lab, row in cars.iterrows() :
    cars.loc[lab, "COUNTRY"] = row["country"].upper()
print(cars)
# Use .apply(str.upper)
cars["COUNTRY"] = cars["country"].apply(str.upper)
print(cars)