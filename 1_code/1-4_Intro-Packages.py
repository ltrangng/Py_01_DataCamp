# PACKAGES

# A package is a directory of Python scripts. Each script is called module. These modules specify functions, methods, and new Python types aimed at solving particular problems.
# Most commonly used for data science are numpy to efficiently work with arrays, matplotlib for data visualization, and scikit-learn for machine learning.

# Install package
# To install packages you can use pip, a package maintenance system for Python.
!pip3 install numpy # install numpy package.

# Import package
# Before using the package, you need to import it first by using import statement.
import numpy
# A commonly used function in numpy is array which takes a list as the input.
array([1, 2, 3]) # return an error.
# To call the array function, you need to refer it to the numpy package with the dot notation.
numpy.array([1, 2, 3])
#  Shorten the numpy prefix by refering to it with a different name.
import numpy as np
np.array([1, 2, 3])
# Suppose you only want to use the array function from the numpy package.
from numpy import array 
array([1, 2, 3]) # no need for dot notation.
# The more standard import numpy is often preferred, as it makes very clear that you are working with the numpy package.

# Math package
# To use the constant pi, you'll need the math package.
import math
# Calculate a circle's circumference
r = 0.43
C = 2 * math.pi * r
A = math.pi ** r
print("Circumference: " + str(C))
# Let's say the Moon's orbit around planet Earth is a perfect circle, with a radius r (in km).
r  = 192500
# Use selective import to import the radians function from math package.
from math import radians
# Calculate the distance travelled by the Moon over 12 degrees of its orbit:
r * radians(12)

# Subpackages
# Packages may contain many subpackages inside. Use not notation to import a function from one of these subpackages
 from scipy.linalg import inv as my_inv
my_inv([[1,2], [3,4]])