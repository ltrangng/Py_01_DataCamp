# DICTIONARIES

# A dictionary is a very useful Python type that can replace traditional lists in many cases.
# Create lists to keep track of  the population in some countries
pop = [30.55, 2.77, 39.21]
countries = ["afghanistan", "albania", "algeria"]
# Suppose you want to know the population of Albania
ind_lb = countries.index["albania"] 
pop[ind_lb] # he list method index() is not so convenient
# Convert these two lists into a dictionary
world = {"afghanistan":30.55, "albania":2.77, "algeria":39.21}
print(world) 
world["albania"] # much more intuitive.

# Create a dictionary
countries = ["spain", "france", "germany", "norway"]
capitals = ["madrid", "paris", "berlin", "oslo"] 
europe = {"spain":"madrid", "france":"paris", "germany":"berlin","norway":"oslo"}
print(europe)
# Accessing the values in a dictionary is easy and intuitive
europe["france"]
# .keys() method gets keys from the dictionary
europe.keys()

# Immutable objects
# The keys in the dictionary should be unique
world = {"afghanistan":30.55, "albania":2.77, "algeria":39.21, "albania": 2.81}
print(world) # the last added key will be kept in the resulting dictionary
# Adding more countries and their capitals to europe
europe["italy"] = "rome"
europe["poland"] = "warsaw"
print(europe)
# Or mess the dictionary up a bit for fun
europe["germany"] = "bonn"
del(europe["spain"])
print(europe)

# Dictionaries in dictionary
# While keys in a dictionary have to be unique, their values are not immutable.
# You can even assign a dictionary as a value within a dictionary.
europe = { "spain": { "capital":"madrid", "population":46.77 }, "france": { "capital":"paris", "population":66.03 }, "germany": { "capital":"berlin", "population":80.62 }, "norway": { "capital":"oslo", "population":5.084 } }
# Using double [][] to access the sub-dictionary inside the dictionary
europe["france"]["capital"]
# Add a sub-dictionary with information for Italy
sub_dict = {"capital":"rome", "population":59.83}
europe["italy"] = sub_dict
print(europe)