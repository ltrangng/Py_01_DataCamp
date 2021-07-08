# PANDAS

# Pandas package
# Pandas package handles tabular dataset. 
import pandas as pd
dict = {"country":["Brazil", "Russia", "India", "China", "South Africa"], 
        "capital":["Brasilia", "Moscow", "New Delhi", "Bejing", "Pretoria"], 
        "area":[8.516, 17.10, 3.286, 9.597, 1.221], 
        "population":[200.4, 143.5, 1252, 1357, 52.98]} 
brics = pd.DataFrame(dict)
brics # pandas automatically assigns row labels, from 0 to 4.
# Specify row labels manually
brics.index = ["BR", "RU", "IN", "CH", "SA"]
brics

# Create a DataFrame
# DataFrame can be created manually from a dictionary like in brics. But mostly it is imported from an external file
# read_csv(): import csv file 
brics = pd.read_csv("https://raw.githubusercontent.com/ltrangng/Py_01_DataCamp/main/0_data/brics.csv")
brics # the row labels are still seen as in their own column.
# Specify the index_col argument in read_csv()
brics = pd.read_csv("https://raw.githubusercontent.com/ltrangng/Py_01_DataCamp/main/0_data/brics.csv", index_col = 0)
brics
# Create manually a dataframe with vehicle data from different countries
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True] # drive left or right
cpc = [809, 731, 588, 18, 200, 70, 45] # number of motor vehicles per 1000 people
# Create a dictionary with these 3 key-values and a list for row labels
my_dict = {"country":names, "drives_right": dr, "cars_per_cap": cpc}
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']
print(my_dict)
# DataFrame(): turn dictionary into a DataFrame
cars = pd.DataFrame(my_dict)
cars.index = row_labels
cars
# More efficiently, import the csv as a DataFrame
cars = pd.read_csv("https://raw.githubusercontent.com/ltrangng/Py_01_DataCamp/main/0_data/cars.csv", index_col = 0)
cars

# Index and select data from DataFrame
# [] and column label allows to access columns in a DataFrame
brics["country"]
# The result is not a sub-DataFrame as expected, but a Pandas series
type(brics["country"])
# Used double [[]] to keep data as DataFrame
type(brics[["country"]])
# Use comma to select more columns
brics[["country", "capital"]]
# [] and ":" allow to access rows
brics[1:4]
# Use [[]] s to print out a DataFrame with both the country and drives_right columns of cars
cars[["country", "drives_right"]]
# Select the first three observations
cars[0:3]

# Ideally we want indexing similar like in 2D Numpy array with [row, column].
brics.loc[["RU", "IN", "CH"]] # select based on labels
brics.loc[["RU", "IN", "CH"], ["country", "capital"]] # select both rows and columns
# To select the entire column, specify it with slicing 
brics.loc[:, ["country", "capital"]]
# iloc is position-or index-based
brics.iloc[[1]]
brics.iloc[[1, 2, 3]]
brics.iloc[[1, 2, 3],[0, 1]]
brics.iloc[:,[0, 1]]
# Use loc or iloc to select the observation corresponding to Japan in cars
cars.loc[["JAP"]]
cars.iloc[[2]]
# Select the observations for Australia and Egypt
cars.loc[["AUS", "EG"]]
cars.iloc[[1, 6]]
# Print out the drives_right value of the row corresponding to Morocco
print(cars.loc["MOR", "drives_right"])
# Print out a sub-DataFrame, containing the observations for Russia and Morocco and the columns country and drives_right
print(cars.loc[["RU", "MOR"], ["country", "drives_right"]])
# Print out both the cars_per_cap and drives_right column as a DataFrame using loc or iloc
cars.loc[:, ["cars_per_cap", "drives_right"]]