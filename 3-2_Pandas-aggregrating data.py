# AGGREGRATING DATA

# Summary statistics
# Summary statistics are numbers that summarize your dataset.
# Import Pandas, NumPy and the dogs dataset
import pandas as pd
import numpy as np
dogs = pd.read_csv("0_data/dogs.csv", index_col = 0)
print(dogs)
# .mean() is one of the most common summary statistics
dogs["height_cm"].mean()
# Summarizing dates
dogs["date_of_birth"].min() # oldest dog
dogs["date_of_birth"].max() # youngest dog
# .agg() allows to compute custom summary statistics
def pct30(column) :             # create a function 
    return column.quantile(0.3) # computes the 30th percentile of a column
dogs["weight_kg"].agg(pct30)
# Use .agg() for multiple summaries
dogs[["weight_kg", "height_cm"]].agg(pct30)
# Define another function that computes the 40th percentile
def pct40(column) :
    return column.quantile(0.4)
dogs["weight_kg"].agg([pct30, pct40])
# Cumulative statistics can also be helpful in tracking summary statistics over time
dogs["weight_kg"].cumsum() # cumulative sum

# Import the sales dataset from the Walmart stores
sales = pd.read_csv("0_data/sales_subset.csv", index_col = 0)
# Explore the dataset
sales.head()
sales.info()
# Summarize weekly_sales
sales["weekly_sales"].mean()
sales["weekly_sales"].median()
# Summarize dates
sales["date"].min()
sales["date"].max()
# Define a custom IQR function
def iqr(column) :
    return column.quantile(0.75) - column.quantile(0.25)
# Compute the IQR of the temperature_c
sales["temperature_c"].agg(iqr)
# Compute IQR for multiple columns
sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg(iqr)
# Subset the DataFrame for store 1
sales_1_1 = sales[sales["store"] == 1]
sales.head()
# Sort sales_1_1 by date
sales_1_1 = sales_1_1.sort_values("date")
# Get the cumulative sum of weekly_sales
sales_1_1["cum_weekly_sales"] = sales_1_1["weekly_sales"].cumsum()
# Get the cumulative max of weekly_sales
sales_1_1["cum_max_sales"] = sales_1_1["weekly_sales"].cummax()
# See the calculated columns 
sales_1_1[["date", "weekly_sales", "cum_weekly_sales", "cum_max_sales"]]

# Counting
# Dropping duplicates
store_types = sales.drop_duplicates(subset = ["store", "type"])
store_types.head()
# Drop duplicate store/department combinations
store_depts = sales.drop_duplicates(subset = ["store", "department"])
store_depts
# Subset the rows where is_holiday is True and drop duplicate dates
holiday_dates = sales[sales["is_holiday"] == True].drop_duplicates(subset = "date")
holiday_dates
# Count the number of stores of each type
store_counts = store_types["type"].value_counts()
store_counts
# Get the proportion of stores of each type
store_props = store_types["type"].value_counts(normalize = True) 
store_props # return the relative frequencies of the unique values
# Count the number of each department number and sort
dept_counts_sorted = store_depts["department"].value_counts(sort = True)
dept_counts_sorted # sorted by frequences
# Get the proportion of departments of each number and sort
dept_props_sorted = store_depts["department"].value_counts(sort = True, normalize = True)
dept_props_sorted

# Grouped summary statistics
# Summary statistics can be useful to compare different groups
dogs[dogs["color"] == "black"]["weight_kg"].mean()
dogs[dogs["color"] == "brown"]["weight_kg"].mean()
dogs[dogs["color"] == "white"]["weight_kg"].mean() # inefficient way 
# Use .groupby() for grouped summaries
dogs.groupby("color")["weight_kg"].mean()
# Multiple grouped summaries
dogs.groupby("color").agg([min, max, sum])
# Group by multiple variables
dogs.groupby(["color", "breed"])["weight_kg"].mean()
# Many groups, many summaries
dogs.groupby(["color", "breed"])[["weight_kg", "height_cm"]].mean()
# Calculate total weekly sales
sales_all = sales["weekly_sales"].sum()
# Subset for different stores, calculate total weekly sales
sales_A = sales[sales["type"] == "A"]["weekly_sales"].sum()
sales_B = sales[sales["type"] == "B"]["weekly_sales"].sum()
sales_C = sales[sales["type"] == "C"]["weekly_sales"].sum()
# Get proportion for each type
sales_propn_by_type = [sales_A, sales_B, sales_C] / sales_all
sales_propn_by_type
# Calculate with groupby
sales_by_type = sales.groupby("type")["weekly_sales"].sum()
sales_propn_by_type = sales_by_type / sum(sales_by_type)
sales_propn_by_type # much neater with .groupby
# Multiple grouped summaries
sales_stats = sales.groupby("type")["weekly_sales"].agg([np.min, np.max, np.mean, np.median])
sales_stats
unempl_fuel_stats = sales.groupby("type")[["unemployment", "fuel_price_usd_per_l"]].agg([np.min, np.max, np.mean, np.median])
unempl_fuel_stats

# Pivot tables
# Pivot tables are the standard way of aggregating data in spreadsheets.
# In pandas, pivot tables are essentially just another way of performing grouped calculations.
# .pivot_table() method is just an alternative to .groupby().
dogs.groupby("color")["weight_kg"].mean()
# is the same as
dogs.pivot_table(values = "weight_kg",
                 index = "color")
# Different statistics
dogs.pivot_table(values = "weight_kg", 
                 index = "color",
                 aggfunc = np.median)
# Pivot on two variables
dogs.groupby(["color", "breed"])["weight_kg"].mean()
# equal to
dogs.pivot_table(values = "weight_kg",
                 index = "color",
                 columns = "breed")
# fill_value replaces missing values with a real value (known as imputation)
dogs.pivot_table(values = "weight_kg", 
                 index = "color",
                 columns = "breed",
                 fill_value = 0)
# Summing with margins argument, which gives the row and column totals of the pivot table contents.
dogs.pivot_table(values = "weight_kg", 
                 index = "color", 
                 columns = "breed",
                 fill_value = 0,
                 margins = True)
# Pivot for mean weekly_sales for each store type
mean_sales_by_type = sales.pivot_table(values = "weekly_sales",
                                       index = "type")
mean_sales_by_type
# Pivot for mean and median weekly_sales for each store type
mean_med_sales_by_type = sales.pivot_table(values = "weekly_sales",
                                           index = "type",
                                           aggfunc = [np.mean, np.median])
mean_med_sales_by_type
# Pivot for mean weekly_sales by store type and holiday 
mean_sales_by_type_holiday = sales.pivot_table(values = "weekly_sales", 
                                               index = "type",
                                               columns = "is_holiday")
mean_sales_by_type_holiday
# Print the mean weekly_sales by department and type; fill missing values with 0s; sum all rows and cols
print(sales.pivot_table(values = "weekly_sales", 
                        index = "department",
                        columns = "type",
                        fill_value = 0,
                        margins = True))