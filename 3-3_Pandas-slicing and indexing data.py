# SLICING AND INDEXING

# Explicit indexes
# Import Pandas, NumPy and the dogs dataset
import pandas as pd
dogs = pd.read_csv("0_data/dogs.csv", index_col = 0)
print(dogs)
# Call out the dataset's columns and indexes
dogs.columns
dogs.index
# Setting a column as an index
dogs_ind = dogs.set_index("name")
print(dogs_ind)
# Remove an index
dogs_ind.reset_index()
# Dropping an index
dogs_ind.reset_index(drop = True) # remove entirely the dog names.
# Indexes make subsetting simpler
dogs[dogs["name"].isin(["Bella", "Stella"])]
# Equivalent code when the names are in the index
dogs_ind.loc[["Bella", "Stella"]]
# Index values don't need to be unique
dogs_ind2 = dogs.set_index("breed")
print(dogs_ind2)
dogs_ind2.loc["Labrador"] # all the labrador data is returned.
# Multi-level indexes or hierarchical indexes
dogs_ind3 = dogs.set_index(["breed", "color"]) # "color" is nested in "breed"
print(dogs_ind3)
# Subset the outer level with a list
dogs_ind3.loc[["Labrador", "Chihuahua"]]
# Subset inner levels with a list of tuples
dogs_ind3.loc[[("Labrador", "brown"), ("Chihuahua", "tan")]]
# Sorting by index values
dogs_ind3.sort_index() # sort from outer to inner level, in ascending order.
# Controlling the sort_index with "level" and "ascending" arguments
dogs_ind3.sort_index(level = ["color", "breed"], 
                     ascending = [True, False])
# Although indexes simplify subsetting, there are downsides:
# Indexes are just data. Storing data in multiple forms makes it harder to think about.
# Indexes violates the "tidy data" principles
# In Pandas, the syntax for working with indexes is different from working with columns.

# Slicing and subsetting with .loc and .iloc
# Slicing is a technique for selecting consecutive elements from objects.
breeds = ["Laborador", "Poodle", "Chow Chow", "Schnauzer", "Laborador", "Chihuahua", "St. Benard"]
# To slice a list, pass first and last positions separated by a ":" in [ ]
breeds[2:5] # Python position starts from 0
# Slice from the begining of the list by omitting 0
breeds[:3]
# Slicing with [:] on its own returns the whole list
breeds[:]
# Slice a DataFrame, firstly sort the index
dogs_srt = dogs.set_index(["breed", "color"]).sort_index()
dogs_srt
# Slicing the outer level index by specifying index values instead of row number
dogs_srt.loc["Chow Chow":"Poodle"] # both positions are inclusive
# Slicing the inner level index does not work that way
dogs_srt.loc["tan":"grey"]
# The correct approach is slicing at inner index levels with tuples
dogs_srt.loc[("Labrador", "brown") : ("Schnauzer", "grey")]
# Slicing columns
dogs_srt.loc[:, "name":"height_cm"] # [:] means "keep everything"
# Slice on rows and columns at the same time
dogs_srt.loc[("Labrador", 'brown'):("Schnauerzer", "grey"), "name":"height_cm"]
# Subset DataFrames by a range of dates
dogs = dogs.set_index("date_of_birth").sort_index()
dogs
dogs.loc["2014-08-25":"2016-09-16"]
# Slicing by partial dates
dogs.loc["2014":"2016"]
# Subsetting by row/column number
dogs.iloc[2:5, 1:4]

# Subsetting and calculation with pivot tables
dogs_height_by_breed_vs_color = dogs.pivot_table(values = "height_cm",
                                                 index = "breed",
                                                 columns = "color")
# Pivot tables are just DataFrames with sorted indexes
dogs_height_by_breed_vs_color.loc["Chow Chow":"Poodle"]
# The methods for calculating summary statistics on DataFrame have axis argument
dogs_height_by_breed_vs_color.mean(axis = "index") # by default calculate rows
dogs_height_by_breed_vs_color.mean(axis = "columns")

# Import temperatures.csv, a DataFrame of average temperatures in cities around the world
temperatures = pd.read_csv("0_data/temperatures.csv", index_col = 0)
temperatures.head()
# Index temperatures by city
temperatures_ind = temperatures.set_index("city")
temperatures_ind
# Reset the index, keeping its contents
temperatures_ind.reset_index()
# Reset the index, dropping its contents
temperatures_ind.reset_index(drop = True)
# Setting an index allows more concise code for subsetting rows via .loc[]
cities = ["Moscow", "Saint Petersburg"]
temperatures[temperatures["city"].isin(cities)]
# Subset temperatures_ind using .loc[]
temperatures_ind.loc[cities]
# Index temperatures by country & city
temperatures_ind2 = temperatures.set_index(["country", "city"])
# Specify two country/city pairs to keep
rows_to_keep = [("Brazil", "Rio De Janeiro"), ("Pakistan", "Lahore")]
temperatures_ind2.loc[rows_to_keep]
# Sorting by index values
temperatures_ind2.sort_index()
temperatures_ind2.sort_index(level = "city")
temperatures_ind2.sort_index(level = ["country", "city"],
                            ascending = [True, False])
# Sort the index of temperatures_ind
temperatures_srt = temperatures_ind2.sort_index()
# Slicing index values
temperatures_srt.loc["Pakistan":"Russia"]
# Try to subset rows from Lahore to Moscow
temperatures_srt.loc["Lahore":"Moscow"] # returns nonsense
# Subset rows from Pakistan, Lahore to Russia, Moscow
temperatures_srt.loc[("Pakistan", "Lahore"):("Russia", "Moscow")]
# Slicing in both directions
temperatures_srt.loc[("India", "Hyderabad"):("Iraq","Baghdad")]
temperatures_srt.loc[:,"date":"avg_temp_c"]
temperatures_srt.loc[("India", "Hyderabab"):("Iraq", "Baghdad"), 
                     "date":"avg_temp_c"]
# Slicing time series
temperatures_bool = temperatures[(temperatures["date"] >= "2010-01-01") & (temperatures["date"] <= "2011-12-31")]
temperatures_bool
# Set date as an index and sort the index
temperatures_ind = temperatures.set_index("date").sort_values("date")
# Use .loc[] to subset temperatures_ind for rows in 2010 and 2011
temperatures_ind.loc["2010-01-01":"2011-12-31"]
# Subsetting by row/column number
temperatures.iloc[22,1]     # 23rd row, 2nd column
temperatures.iloc[:5]       # first 5 rows
temperatures.iloc[:, 2:4]   # columns 3 to 4
temperatures.iloc[0:5, 2:4] # slicing in both directions at once
# Convert the values in "date" column to datetime object
temperatures["date"] = pd.to_datetime(temperatures["date"], format = "%Y-%m-%d")
# Access the components of a date (year, month and day) using code of the form dataframe["column"].dt.component
temperatures["year"] = temperatures["date"].dt.year
# Pivot avg_temp_c by country and city vs year
temp_by_country_city_vs_year = temperatures.pivot_table(values = "avg_temp_c", index = ["country", "city"], columns = "year")
temp_by_country_city_vs_year
# Subsetting pivot tables
temp_by_country_city_vs_year.loc["Egypt":"India"]
temp_by_country_city_vs_year.loc[("Egypt", "Cairo"):("India", "Delhi")]
temp_by_country_city_vs_year.loc[("Egypt", "Cairo"):("India", "Delhi"), "2005":"2010"]
# Calculating on a pivot table
mean_temp_by_year = temp_by_country_city_vs_year.mean() # by year
# Filter for the year that had the highest mean temp
mean_temp_by_year[mean_temp_by_year == mean_temp_by_year.max()]
# Get the mean temp by city
mean_temp_by_city = temp_by_country_city_vs_year.mean(axis = "columns")
# Filter for the city that had the lowest mean temp
mean_temp_by_city[mean_temp_by_city == mean_temp_by_city.min()]