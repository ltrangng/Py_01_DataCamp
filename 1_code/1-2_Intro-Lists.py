# LISTS

# A Python list store data points. E.g, measure the height of everybody in your family:
height1 = 1.73
height2 = 1.68
height3 = 1.71
height4 = 1.89
# Instead of creating variables, store these information in a list
fam = [1.73, 1.68, 1.71, 1.89]
print(fam)
# The values, or elements in a list can be any type.
fam = ["liz", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89] # add strings.
print(fam)
# Lists also can contain lists themselves.
fam2 = [["liz", 1.73],
        ["emma", 1.68],
        ["mom", 1.71],
        ["dad", 1.89]] # sublists are wrapped with square brackets and separated with commas
# Lists are also a Python type with a specific functionality and behaviour.
type(fam)
type(fam2)

# Create a list
# A list is a compound data type; you can group values together.
a = "is"
b = "nice"
my_list = ["my", "list", a, b]
# Collect some information on the house you're living in
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50
# Create a list that contains the area of all the rooms
areas = [hall, kit, liv, bed, bath]
print(areas)
# Add strings to the list
areas = ["hallway", hall, "kitchen", kit, "living room", liv, "bedroom", bed, "bathroom", bath]
print(areas)
# You can also create a list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed],
         ["bathroom", bath]]
print(house)
# A list can contain any Python type. But a list itself is also a Python type.
print(type(house))

# Subsetting lists 
# Python uses index to access information in the list. E.g, the first element in the list has the index 0, the second has index 1 and so on. 
fam[3] # the height of Emma 
# Count backwards using negative indices
fam[-1] # the height of dad
# Slicing allows you to select multiple elements from a list with syntax [start(inclusive):end(exclusive)]
fam[3:5] # index 3 and 4 are return, but index 5 is not included.
# You can also choose to leave out the index before or after the colon.
fam[:4] # starts from index 0.
fam[5:] # include all elements up to and include the last element in the list.
# After you've extracted values from a list, you can use them to perform additional calculations. 
eat_sleep_area = areas[3] + areas[-3]
eat_sleep_area
# Use slicing to create a lists from areas
downstairs = areas[:6]
print(downstairs)
upstairs = areas[6:]
print(upstairs)
# Subset lists using []
house[-1][1] # select the second element of the last index, which is the area of bathroom.

# Manipulating lists
# Changing list elements is pretty straightforward in Python
fam[7] = 1.86
print(fam) # the new value is updated.
fam[0:2] = ["lisa", 1.74]
# Adding elements in the list with + operator
fam_ext = fam + ["me", 1.79]
print(fam_ext)
# Removing elements from a list using del():
del(fam[2])
print(fam)
# Update the area of the bathroom area in the areas
areas[-1] = 10.5
# Make the areas list more trendy by changing "living room" to "chill zone":
areas[4] = "chill zone"
# Add a poolhouse and a garage.
areas_1 = areas + ["poolhouse", 24.5]
areas_2 = areas_1 + ["garage", 15.45]
# Remove the corresponding string and float from the areas list
del(areas[-4:-2])
# To make a copy of the areas list to prevent changes from also taking effect, use [:]
areas_copy = areas[:]
areas_copy[0] = 5.0 # change areas_copy.
# Check out both areas and areas_copy:
print(areas)
print(areas_copy)    
    