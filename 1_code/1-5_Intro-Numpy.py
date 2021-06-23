# NUMPY

# Python lists are powerful objects but cannot carry on operations over entire collection of values. 
# Take the example of the family heights. Add a list of weights respectively:
height = [1.73, 1.68, 1.71, 1.89, 1.79]
weight = [65.4, 59.2, 63.6, 88.4, 68.7] 
# Calculate the Body Mass Index for each family member:
bmi = weight / height ** 2 # returns an error

# Numpy array is similar like the traditional lists, but allows to perform calculations over entire arrays. 
# First import the Numpy package to be able to use the array function
import numpy as np
np_height = np.array(height)
np_weight = np.array(weight)
# Calculatate the BMI again with the new array variables
bmi = np_weight / np_height ** 2
print(bmi) # The calcuations were performed element-wise.
# Numpy can do calculations easily with values of a single type. For different types, the resulting Numpy array will contain a single type. 
np.array([1.0, "is", True]) # converts all elements into strings.
# Get elements from the array using []:
python_list = [1, 2, 3]
numpy_array = np.array([4, 5, 6])
# Subsetting list using an array of Booleans 
bmi > 23
bmi[bmi > 23]

# You receive a list of baseball players' height in inches
from numpy import genfromtxt
height_in = genfromtxt("https://raw.githubusercontent.com/ltrangng/Py_01_DataCamp/main/0_data/height_in.csv", dtype = "int", delimiter=',')
np_height_in = np.array(height_in)
# Convert height from inches to meters
np_height_m = np_height_in * 0.0254
print(np_height_m)
# You also receive a list of weight in pounds
weight_lb = genfromtxt("https://raw.githubusercontent.com/ltrangng/Py_01_DataCamp/main/0_data/weight_lb.csv", dtype = "int", delimiter = ",")
np_weight_lb = np.array(weight_lb)
# Convert weight from pounds to kilograms
np_weight_kg = np_weight_lb * 0.453592
print(np_weight_kg)
# Use np_height_m and np_weight_kg to calculate the BMI of each player using the BMI equation
bmi = np_weight_kg / np_height_m ** 2
print(bmi)
# Subsetting a Numpy array is similar to subsetting a Python list with []
weight_lb[50] # weight at index 50.
weight_lb[100:111] # slicing like in lists
# Use a boolean array to make a selection of lightweight baseball players
light = bmi < 21
print(bmi[light])

# 2D Numpy array
# Ask Python for the type of these arrays
type(np_weight_kg) # ndarray stands for n-dimensional array
# Create more dimensional arrays
np_2d = np.array([height, weight])
print(np_2d) # the result has two dimensions
# shape is an attribute of an Numpy array that gives more information about what the data structure looks like
np_2d.shape # shape uses dot notation similar like methods, it does not require () which indicates a function.
# Also in 2D arrays, the Numpy rule applies: an array can contain only a single type.
np.array([[1.73, 1.68, 1.71, 1.89, 1.79],[65.4, 59.2, 63.6, 88.4,"68.7"]]) # all elements are coerced into strings
# Restructure the BMI information in a 2D numpy array
baseball = genfromtxt("https://raw.githubusercontent.com/ltrangng/Py_01_DataCamp/main/0_data/baseball_2d.csv", dtype = "int", delimiter = ",")
np_baseball = np.array(baseball)
print(np_baseball)

# 2D Arithmetic
# Numpy is also able to perform all calculations element-wise in 2D arrays.
# np_baseball is coded this time as a 2D array with 3 columns representing height (in inches), weight (in pounds) and age (in years)
baseball = genfromtxt("https://raw.githubusercontent.com/ltrangng/Py_01_DataCamp/main/0_data/baseball_2d-2.csv", dtype = "int", delimiter = ",")
np_baseball = np.array(baseball)
print(np_baseball)
#  convert the units of height and weight to metric
conversion = np.array([0.0254, 0.453592, 1]) # inches to meters, pounds to kilograms
print(np_baseball * conversion)

# Basic statistics
# Numpy also allows you to do do some basic statistics. 
# Find out the average height of baseball players with np.mean()
np_height_in = np_baseball[:,0] # choose the first column, which contains height values.
np.mean(np_height_in)
# Average weight
np_weight_lb = np_baseball[:,1]
np.mean(np_weight_lb)
# Similarly, we can find out the median values
np.median(np_weight_lb)
np.median(np_height_in)
# corrcoef checks if there is a correlation
np.corrcoef(np_weight_lb, np_height_in)
# std() for standard deviation
np.std(np_height_in)
# Numpy also features more basic functions like sum() and sort(), which also exist in the basic Python distribuition. 
# The big difference is the speed. Numpy enforces a single data type so it can drastically speed up the calculations