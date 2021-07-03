# MATPLOTLIB

# There are many data visualization packages, but mostly used is matplotlib.
# Import the subpackage pyplot of matplotlib as plt by convention
import matplotlib.pyplot as plt
# Let's try to gain some insights in the evolution of the world population
year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972] # expressed in billions
# Call plt.plot() and use our two lists as arguments
plt.plot(year, pop) 
plt.show()
# plt.plot() tells Python what to plot and how to plot it. plt.show() actually displays the plot
# Another type of plot is the scatter plot. 
plt.scatter(year, pop)
plt.show()

# Line plot
# Examine line plots for larger dataset, e.g, the World Bank's estimation of the world population
from numpy import genfromtxt
year = genfromtxt("https://raw.githubusercontent.com/ltrangng/Py_01_DataCamp/main/0_data/year.csv", dtype = "int", delimiter = ",")
pop = genfromtxt("https://raw.githubusercontent.com/ltrangng/Py_01_DataCamp/main/0_data/pop.csv", dtype = "float", delimiter = ",")
# Print the last item to see the predicted population in 2100
print(year[-1])
print(pop[-1])
# Make a line plot: year on the x-axis, pop on the y-axis
plt.plot(year, pop)
plt.show() # the plot looks more smooth now because there are more data points.
# Import the gapminder data from Hans Rosling that was collected in 2007
life_exp = genfromtxt("https://raw.githubusercontent.com/ltrangng/Py_01_DataCamp/main/0_data/life_exp.csv", dtype = "float", delimiter = ",")
gdp_cap = genfromtxt("https://raw.githubusercontent.com/ltrangng/Py_01_DataCamp/main/0_data/gdp_cap.csv", dtype = "float", delimiter = ",")
# Print the last item from both the list. It's information about Zimbawe.
print(life_exp[-1])
print(gdp_cap[-1])
# Build a line chart, with gdp_cap on the x-axis, and life_exp on the y-axis
plt.plot(gdp_cap, life_exp)
plt.show() # the line doesn't make much sense.

# Scatter plot
# Scatter plot is a better choice for assessing if there is a correlation between two variables.
plt.scatter(gdp_cap, life_exp)
plt.show()
# A correlation will become clear when you display the variables on logarithmic scale
plt.scatter(gdp_cap, life_exp)
plt.xscale("log")
plt.show() # positive correlation
# How about a relationship between population and life expectancy of a country? 
pop_2007 = genfromtxt("https://raw.githubusercontent.com/ltrangng/Py_01_DataCamp/main/0_data/pop_2007.csv", dtype = "float", delimiter = ",")
plt.scatter(pop_2007,life_exp)
plt.show() # no clear correlation, which makes sense.

# Histogram
# Histogram is a type of visualization that is very useful to explore the distribution of the variables.
# Generate a histogram with the list of 12 values
values = [0,0.6,1.4,1.6,2.2,2.5,2.6,3.2,3.5,3.9,4.2,6]
plt.hist(values, bins = 3)
plt.show()
# Create a histogram for life_exp to see how life expectancy in different countries is distributed
plt.hist(life_exp)
plt.show()
# by default, Python sets the number of bins to 10. Experiment with different numbers of bins
plt.hist(life_exp, bins = 5)
plt.show()
plt.clf() # clear the plot.
plt.hist(life_exp, bins = 20)
plt.show()
plt.clf()
# The histogram makes it easy to compare, e.g, life expectancy in 2007 and in 1950.
life_exp_1950 = genfromtxt("https://raw.githubusercontent.com/ltrangng/Py_01_DataCamp/main/0_data/life_exp_1950.csv", dtype = "float", delimiter = ",")
# Build two histograms to see the difference
plt.hist(life_exp, bins = 15)
plt.show()
plt.clf()
plt.hist(life_exp_1950, bins = 15)
plt.show()
plt.clf()

# Customization
# Adding labels to the x and y axes
plt.plot(year, pop)
plt.xlabel("Year")
plt.ylabel("Population")
plt.show()
# Add title
plt.plot(year, pop)
plt.xlabel("Year")
plt.ylabel("Population")
plt.title("World Population Projections")
plt.show()
# Use plt.yticks() to put the population growth in perspective 
plt.plot(year, pop)
plt.xlabel("Year")
plt.ylabel("Population")
plt.title("World Population Projections")
plt.yticks([0, 2, 4, 6, 8, 10], ["0", "2B", "4B", "6B", "8B", "10B"])
plt.show()
# Customize the scatter plot of life expectancy vs. GDP per capita
plt.scatter(gdp_cap, life_exp)
plt.xscale("log")
plt.xlabel("GDP per Capital [in USD]")
plt.ylabel("Life Expectancy [in years]")
plt.title("World Development in 2007")
plt.xticks([1000, 10000, 100000], ['1k', '10k', '100k'])
plt.show()
# Change the size of the dots so that they corresponds to the population
plt.scatter(gdp_cap, life_exp, s = pop_2007)
plt.xscale("log")
plt.show
# Increasing the size of the bubbles will make things stand out more
import numpy as np
np_pop = np.array(pop_2007)
plt.scatter(gdp_cap, life_exp, s = np_pop * 2)
plt.xscale("log")
plt.show()
# Make the plot more colorful
dict = {
    'Asia':'red',
    'Europe':'green',
    'Africa':'blue',
    'Americas':'yellow',
    'Oceania':'black'
}
col = ['red', 'green', 'blue', 'blue', 'yellow', 'black', 'green', 'red', 'red', 'green', 'blue', 'yellow', 'green', 'blue', 'yellow', 'green', 'blue', 'blue', 'red', 'blue', 'yellow', 'blue', 'blue', 'yellow', 'red', 'yellow', 'blue', 'blue', 'blue', 'yellow', 'blue', 'green', 'yellow', 'green', 'green', 'blue', 'yellow', 'yellow', 'blue', 'yellow', 'blue', 'blue', 'blue', 'green', 'green', 'blue', 'blue', 'green', 'blue', 'green', 'yellow', 'blue', 'blue', 'yellow', 'yellow', 'red', 'green', 'green', 'red', 'red', 'red', 'red', 'green', 'red', 'green', 'yellow', 'red', 'red', 'blue', 'red', 'red', 'red', 'red', 'blue', 'blue', 'blue', 'blue', 'blue', 'red', 'blue', 'blue', 'blue', 'yellow', 'red', 'green', 'blue', 'blue', 'red', 'blue', 'red', 'green', 'black', 'yellow', 'blue', 'blue', 'green', 'red', 'red', 'yellow', 'yellow', 'yellow', 'red', 'green', 'green', 'yellow', 'blue', 'green', 'blue', 'blue', 'red', 'blue', 'green', 'blue', 'red', 'green', 'green', 'blue', 'blue', 'green', 'red', 'blue', 'blue', 'green', 'green', 'red', 'red', 'blue', 'red', 'blue', 'yellow', 'blue', 'green', 'blue', 'green', 'yellow', 'yellow', 'yellow', 'red', 'red', 'red', 'blue', 'blue']
plt.scatter(gdp_cap, life_exp, s = np_pop * 2, c = col)
plt.xscale("log")
plt.show()
# Change the opacity of the bubbles so that the plot is more readable
plt.scatter(gdp_cap, life_exp, s = np_pop * 2, c = col, alpha = 0.6)
plt.xscale("log")
plt.show()
# Additional customizations like plt.grid(True) turns the gridlines on, and plt.text() adds text on the plot
plt.scatter(gdp_cap, life_exp, s = np_pop * 2, c = col, alpha = 0.6)
plt.xscale("log")
plt.grid(True)
plt.text(1550, 71, "India")
plt.text(5700, 80, "China")
plt.show()
# Put every customization together
plt.scatter(gdp_cap, life_exp, s = np_pop * 2, c = col, alpha = 0.6 )
plt.xscale("log")
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000], ['1k', '10k', '100k'])
plt.grid(True)
plt.text(1550, 71, 'India')
plt.text(5700, 80, 'China')
plt.show()