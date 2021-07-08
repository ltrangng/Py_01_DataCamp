# TRANSFORMING DATA 

# DataFrames
# Pandas uses rectangular data, or tabular data, which is the most common form to store data.
import pandas as pd
# In Pandas, rectangular data is represented as a DataFrame object
dogs = pd.read_csv("https://raw.githubusercontent.com/ltrangng/Py_01_DataCamp/main/0_data/dogs.csv", 
                   index_col = 0)
print(dogs)
# Quickly explore the DataFrame to get a sense of its content
dogs.head() # returns first few rows of the DataFrame
dogs.info() # displays column names, data types and whether there is missing values
dogs.shape  # attribute contains a tulpe that holds the number of rows and columns
dogs.describe()  # compute some summary statistics for numerical columns.
# DataFrames consist of 2 different components, accessible using attributes
dogs.values  # contains the data values in 2D NumPy array
dogs.columns # contains column names
dogs.index   # contains row number or row names

# Import homelessness.csv file, a DataFrame containing estimates of homelessness in each U.S. state in 2018.
homelessness = pd.read_csv("https://raw.githubusercontent.com/ltrangng/Py_01_DataCamp/main/0_data/homelessness.csv", 
                       index_col = 0)
# Inspect the DataFrame
homelessness.head()
# Print information about the column types and missing values
print(homelessness.info())
# Print out the DataFrame shape
print(homelessness.shape)
# Print the DataFrame's description
print(homelessness.describe())

# Sorting and subsetting
# Sorting change the order of the rows so that the most interesting data is on top of the DataFrame
dogs.sort_values("weight_kg")
