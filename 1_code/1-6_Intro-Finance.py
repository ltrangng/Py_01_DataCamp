# INTRODUCTION TO PYTHON IN FINANCE

# You might want to use Python in finance for:
    # To compile monthly sales report
    # To optimize an investment strategies performance
    # Visualizing stock data trends
    
# Outputs in iPython vs. script.py
1 + 1
print(1 + 1)
# But in script.py, if you don't specify print(), no ouput would be displayed.

# Variables
# Variables consist of two parts: the name and the value
day_2 = 5 # correct
2_day = 5 # incorrect, variable name can't start with a number
# Using variables to evaluate stock trends
price = 200 # 200$ per share, market price
earnings = 5 # 5$ earning per share
pe_ratio = price / earnings
print(pe_ratio)
# Finding the total revenue
revenue_1 = 229.23
revenue_2 = 177.86
revenue_3 = 89.95
total = revenue_1 + revenue_2 + revenue_3
print(total)
# Finding the average revenue
average = total /3 
print(average)

# Data types
# 4 types of data in Python:
    # strings (str): "hello world!" 
    # integers (int): 40 
    # floats (float): 3.14
    # Booleans (bool): True or False
# Identify data type of a variable with type()
company_1 = "Apple" # string
type(company_1)     
year_1 = 2017       # integer 
type(year_1)        
revenue_1 = 229.23  # float
type(revenue_1)
# Booleans in Python
test_company = "apple"     # strings are case-sensitive in Python
company_1 == test_company
revenue_1 > revenue_2
# Variable manipulations
x = 5
print(x * 3)
y = "stock"
print(y * 3)
# Add integers
print(x + 3)
# Add integers to strings
print(y + 3) # return error
# Convert variable types
pi = 3.14
type(pi)
pi_str = str(pi)
type(pi_str)
# Combining data types
year_1_str = str(year_1) 
revenue_1_str = str(revenue_1)
# Create a complete sentence combining only the string data types
sentence = "The revenue of " + company_1 + " in " + year_1_str + " was $" + revenue_1_str + " billion."
print(sentence)

# Lists
# A list in Python can contain any number of elements
names = ["Apple Inc", "Coca-Cola", "Walmart"]
print(names)
prices = [159.54, 37.13, 71.17]
print(prices)
# Indexing list items
print(names[0])  # first item
print(names[1])  # second item
print(prices[-1]) # last item
# Slicing multiple list elements
names_subset = names[1:3]   # subset the last 2 elements
print(names_subset)
prices_subset = prices[0:2] # subset the first 2 elements
print(prices_subset)
# Lists in lists
stocks = [names, prices]
print(stocks)
# List indexing
print(stocks[1])    # obtain the list of prices
print(stocks[0][1]) # obtain company name Coca-cola
print(stocks[1][2]) # obtain price of Coca-cola

# Methods vs. functions
# While all methods are functions, not all functions are methods:
    # Functions take an object as input (pass an object)
    # Methods act on 
# For lists, useful functions include max() and min()
price_max = max(prices) # function
print(price_max)
# A useful list method is .sort() which sorts the elements in a list.
prices.sort() # method
print(prices)
# The .append() method increases the length of the list by one
names.append("Amazon.com")
print(names)
# The .extend() method increases the length of the list by the number of elements 
more_elements = ["DowDuPont", "Alphabet Inc"]
names.extend(more_elements)
print(names)
# The method .index() returns the index of the element specified
max_index = prices.index(price_max)
max_stock_name = names[max_index]
print("The largest stock price is associated with " + max_stock_name + " and is $" + str(price_max) + ".")

# Arrays
# NumPy arrays are optimized for numerical analyses and contain only a single data type. 
# Install and import Numpy package
conda install numpy
import numpy as np # import with an alias
# array() converts a list into an array
prices = [170.12, 93.29, 55.28, 145.30, 171.81, 59.50, 100.50]
earnings = [9.2, 5.31, 2.41, 5.91, 15.42, 2.51, 6.79]
prices_array = np.array(prices) # use alias to indicate that the function comes from Numpy 
earnings_array = np.array(earnings)
print(prices_array)
print(earnings_array)
# Elementwise operations on arrays
pe_array = prices_array/earnings_array
print(pe_array)
# Subsetting elements from an array
prices_array[0:3]   # subset first 3 elements
prices_array[-3:]   # subset last 3 elements
prices_array[0:7:3] # subset every third element
# Creating a 2D array
stock_array = np.array([prices, earnings])
print(stock_array)
# Check out the shape and size of the 2D array
print(stock_array.shape)
print(stock_array.size)
# numpy.transpose() switches rows and columns of a numpy array
stock_array_transposed = np.transpose(stock_array)
print(stock_array_transposed)
# The size of the 2D array remains the same but the shape changes
print(stock_array_transposed.shape)
print(stock_array_transposed.size)
# Subsetting 2D arrays is similar to subsetting nested lists
stock_array_transposed[:, 0] # subset first column (prices)
stock_array_transposed[:, 1] # subset second column (earnings)
stock_array_transposed[0,:]  # subset the price and earning of the first company
# Calculating array stats
print(np.mean(prices)) # calculate mean price
print(np.std(prices))  # calculate standard deviation
# Generating a sequence of numbers
print(np.arange(1, 8))    # by default the increment = 1
print(np.arange(1, 8, 2)) # sequence of odd number with formula (start, stop, step)
# Using arrays for analysis: Who's above average?
price_mean = np.mean(prices)          # find the mean price
boolean_array = (prices > price_mean) # create boolean array
above_avg = prices[boolean_array]     # select prices above average
print(above_avg)
# Add arrays of companies with their associated sectors
companies = np.array(['Apple Inc', 'Abbvie Inc', 'Abbott Laboratories', 'Accenture Technologies', 'Allergan Plc'])
sectors = np.array(['Information Technology', 'Health Care', 'Health Care', 'Information Technologies', 'Health Care'])
# Who's in healthcare?
boolean_array = (sectors == "Health Care")
healthcare = companies[boolean_array]
print(healthcare)

# Visualization in Python
# Load Pyplot from the package Matplotlib and datasets to visualize
import matplotlib.pyplot as plt
days = open("0_data/days.csv", "r").read().split(", ")
days = [int(x) for x in days]
days_short = open("0_data/days_short.csv", "r").read().split(", ")
days_short = [int(x) for x in days_short]
prices = open("0_data/", "r").read().split(", ")
prices = [float(x) for x in prices]
prices1 = open("0_data/prices1.csv", "r").read().split(", ")
prices1 = [float(x) for x in prices1]
prices2 = open("0_data/prices2.csv", "r").read().split(", ")
prices2 = [float(x) for x in prices2]

# Plot the price of stock over time
plt.plot(days, prices, color = "red", linestyle = "--")
# Display the plot
plt.show()
# Adding axis labels and titles
plt.xlabel("Days")
plt.ylabel("Prices, $")
plt.title('Company Stock Prices Over Time')
plt.show()
# Multiple lines on the same plot
plt.plot(days_short, prices1, color = "green")
plt.plot(days_short, prices2, color = "red")
plt.xlabel('Days')
plt.ylabel('Prices, $')
plt.title('Stock Prices Over Time')
plt.show()
# Scatterplots
plt.scatter(days, prices, color = "green", s = 0.1)
plt.show()
# Histograms
plt.hist(prices, bins = 100)
plt.show()
# Comparing two histograms
plt.hist(prices1, bins = 100, alpha = 0.4)
plt.hist(prices2, bins = 100, alpha = 0.4)
# Adding a legend
plt.hist(prices1, bins = 100, alpha = 0.4, label = "Price 1")
plt.hist(prices2, bins = 100, alpha = 0.4, label = "Price 2")
plt.legend()
plt.show()