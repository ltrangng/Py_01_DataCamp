# CREATING AND VISUALIZING DATA

# Import libraries and the avocado dataset which contains weekly US avocado sales data
import pandas as pd
import matplotlib.pyplot as plt

avocados = pd.read_csv("0_data/avocados.csv")
avocados.head()
# Get the total number of avocados sold of each size
nb_sold_by_size = avocados.groupby("size")["nb_sold"].sum()
# Create a bar plot of the number of avocados sold by size
nb_sold_by_size.plot(kind = "bar")
plt.show() # extra large avocados are not so popular.
# Changes in sales over time
nb_sold_by_date = avocados.groupby("date")["nb_sold"].sum()
nb_sold_by_date.plot(kind = "line") # number of avocado sales peak
# Avocado supply and demand
avocados.plot(x = "nb_sold", y = "avg_price", kind = "scatter",
              title = "Number of avocados sold vs. average price")

# Missing values
# Import the avocado dataset for the year 2016
avocados_2016 = pd.read_csv("0_data/avocados_2016.csv", index_col = False, na_values = "NaN")
avocados_2016.head()
avocados_2016.info()
# Check individual values for missing values
avocados_2016.isna()
# Check each column for missing values
avocados_2016.isna().any().sum()
# Bar plot of missing values by variable
avocados_2016.isna().sum().plot(kind = "bar")
plt.show()
# Remove rows with missing values
avocados_complete = avocados_2016.dropna()
avocados_complete.isna().any()
# Replacing missing values
cols_with_missing = ["small_sold", "large_sold", "xl_sold"]
# Create histograms showing the distributions cols_with_missing
avocados_2016[cols_with_missing].hist()
plt.show()
# Fill in missing values with 0
avocados_filled = avocados_2016.fillna(0)
# Create histograms of the filled columns
avocados_filled[cols_with_missing].hist()
plt.show()

# Creating DataFrames
# Create a list of dictionaries with new data
avocados_list = [{"date": "2019-11-03", "small_sold": 10376832, "large_sold": 7835071}, 
                 {"date": "2019-11-10", "small_sold": 10717154, "large_sold": 8561348}]
# Convert list into DataFrame
avocados_2019 = pd.DataFrame(avocados_list)
# Create a dictionary of lists with new data
avocados_dict = {"date": ["2019-11-17", "2019-12-01"], 
                 "small_sold": [10859987, 9291631],
                 "large_sold": [7674135, 6238096]}
# Convert dictionary into DataFrame
avocados_2019 = pd.DataFrame(avocados_dict)
avocados_2019

# Reading and writing CSVs
airline_bumping = pd.read_csv("0_data/airline_bumping.csv")
airline_bumping.head()
# For each airline, select nb_bumped and total_passengers and sum
airline_totals = airline_bumping.groupby("airline")[["nb_bumped", "total_passengers"]].sum()
# Create new col, bumps_per_10k: no. of bumps per 10k passengers for each airline
airline_totals["bumps_per_10k"] = airline_totals["nb_bumped"] / airline_totals["total_passengers"] * 10000
airline_totals
# DataFrame to csv
airline_totals_sorted = airline_totals.sort_values("bumps_per_10k", ascending = False)
airline_totals_sorted
airline_totals_sorted.to_csv("0_data/airline_totals_sorted.csv")