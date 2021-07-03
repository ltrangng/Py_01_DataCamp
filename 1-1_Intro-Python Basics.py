# PYTHON BASICS

# The Python Interface
# In the Python script, you can type Python code, save it in script.py. The script is then executed in IPython Shell.
# Python can be used for quick calculations.
print(5 / 8)
print(7 + 10)
# Add comment by using the # tag. These comments are not run as Python code, so they won't influence your result. 
print(5 / 8)  # division
print(7 + 10) # addition

# Python as a calculator
print(2 + 3)  # addition
print(5 - 3)  # substraction
print(2 * 3)  # multiplication
print(15 / 5) # division
print(2 ** 3) # exponential
print(10 % 3) # modulo
# Suppose you have 100 dollars, which you can invest with a 10% return each year. After one year, it's 100 × 1.1 = 110 dollars, and after two years it's 100 × 1.1 × 1.1 = 121 dollars. How much is your 100 dolalrs worth after 7 years?
print(100 * 1.1 ** 7)

# Variables
# If you want to do more complex calculations, you will want to "save" values while you are coding along by defining a variable with specific, case-sensitive name. The variable can be assigned with an = sign. You can then use it later by typing the variable name.
height = 1.79
weight = 68.7
print(height)
print(weight)
# Calculate the Body mass index (or BMI) and store the value
bmi = weight / height ** 2
print(bmi)
# Change the weight and run the bmi calcuation again
weight = 74.2
bmi = weight / height ** 2
print(bmi)

# Python types
# data type represents numerical values like int (interger) and float (floating point).
# a str (string) represents text in single ' or double quotes "
# a Boolean (bool) is a type that can be either True or False.
# Check the data type with the type() function.
type(bmi)
type(5)
type("body max index")
type(True)

# Create a variable savings with the value 100
savings = 100
print(savings)
# Instead of calculating your savings with actual values, we can use variables instead. 
growth_multiplier = 1.1
result = savings * growth_multiplier ** 7
print(result)
# Create other variables that store different types and check out their types:
desc = "compound interest"
type(desc)    
profitable = True
type(profitable)
# Different types behave differently in Python.
year1 = savings + 10
print(year1)
doubledesc = desc + desc
print(doubledesc)
# The + operator, however, does not add a float to a string, because numeric and character values cannot be summed together. 
print("I started with $" + savings + " and now have $" + result + ". Awesome!")
# To fix the error, you'll need to explicitly convert the types of your variables. 
# str(): converts a value into a string. 
# float(): converts a value into a floating point.
# int(): converts a value into an integer.
# bool(): converts a value into a boolean.
print("I started with $" + str(savings) + " and now have $" + str(result) + ". Awesome!")