# TRANSFORMING DATA 

# DataFrames
# Pandas uses rectangular data, or tabular data, which is the most common form to store data.
import pandas as pd
# In Pandas, rectangular data is represented as a DataFrame object
dict = {"name":["Bella", "Charlie", "Lucy", "Cooper", "Max", "Stella", "Bernie"],
        "breed":["Labrador", "Poodle", "Chow Chow", "Schnauzer", "Labrador", "Chihuahua", "St. Bernard"],
        "color":["brown", "black", "brown", "gray", "black", "tan", "white"],
        "height_cm":[56, 43, 46, 49, 59, 18, 77],
        "weight_kg":[24, 24, 24, 17, 29, 2, 74],
        "date_of_birth":["2013-07-01", "2016-09-16", "2014-08-25", "2011-12-11", "2017-01-20", "2015-04-20", "2018-02-27"]}
dogs = pd.DataFrame(dict) 
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

# Sorting and subsetting
# Sorting change the order of the rows so that the most interesting data is on top of the DataFrame
dogs.sort_values("height_cm") # sort in ascending order
# Sort by multiple variables
dogs.sort_values(["weight_kg", "height_cm"]) # sort first by weight, then height
# To change the direction values are sorted in, pass a list to the ascending argument
dogs.sort_values(["weight_kg", "height_cm"], ascending = [True, False])
# Subsetting columns
dogs["name"]
# Select multiple columns
dogs[["breed", "height_cm"]]
# Subset rows with logical value
dogs[dogs["height_cm"] > 50]
# Subseting based on text data
dogs[dogs["breed"] == "Labrador"]  
# Subsetting based on dates
dogs[dogs["date_of_birth"] > "2015-01-01"]
# Subsetting based on multiple conditions
is_lab = dogs["breed"] == "Labrador"
is_brown = dogs["color"] == "brown"
dogs[is_lab & is_brown]
# isin() method: takes in a list of values to filter for
is_black_or_brown = dogs["color"].isin(["black", "brown"])
dogs[is_black_or_brown]

# New columns
# Add a new column
dogs["height_m"] = dogs["height_cm"] / 100
print(dogs)
# Calculate the BMI of the dogs
dogs["bmi"] = dogs["weight_kg"] / dogs["height_m"] ** 2
print(dogs)
# Multiple manipulations
bmi_lt_100 = dogs[dogs["bmi"] < 100] # skinny dogs
bmi_lt_100_height = bmi_lt_100.sort_values("height_cm", ascending = False) # tall dogs
bmi_lt_100_height[["name", "height_cm", "bmi"]] # keep only columns we're interested in.

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
# Sort by individuals
homelessness.sort_values("individuals")
# Sort by descending family members
homelessness.sort_values("family_members", ascending = False)
# Sort by region, then descending family members
homelessness.sort_values(["region", "family_members"], ascending = [True, False])
# Create a DataFrame that contains only the individuals column 
individuals = homelessness["individuals"]
# Print the head of the result
print(individuals.head())
# Select the state and family_members columns
state_fam = homelessness[["state", "family_members"]]
print(state_fam.head())
# Filter for rows where individuals is greater than 10000
homelessness[homelessness["individuals"] > 10000]
# Filter for rows where region is Mountain
homelessness[homelessness["region"] == "Mountain"]
# Filter for rows where family_members is less than 1000  and region is Pacific
homelessness[(homelessness["region"] == "Pacific") & (homelessness["family_members"] < 1000)]
# Subset for rows in South Atlantic or Mid-Atlantic regions
homelessness[homelessness["region"].isin(["Atlantic", "Mid-Atlantic"])]
# Add a new column as sum of individuals and family_members
homelessness["total"] = homelessness["individuals"] + homelessness["family_members"]
# Add a new column as proportion of individuals
homelessness["p_individuals"] = homelessness["individuals"] / homelessness["total"]
print(homelessness)
# Create a new column as homeless individuals per 10k state pop
homelessness["indiv_per_10k"] = 10000 * homelessness["individuals"] / homelessness["state_pop"]
# Subset rows for indiv_per_10k greater than 20
high_homelessness = homelessness[homelessness["indiv_per_10k"] > 20]
# Sort high_homelessness by descending indiv_per_10k
high_homelessness_srt = high_homelessness.sort_values("indiv_per_10k", ascending = False)
# From high_homelessness_srt, select the state and indiv_per_10k columns
result = high_homelessness[["state", "indiv_per_10k"]]
print(result)