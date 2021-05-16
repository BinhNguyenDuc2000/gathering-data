#Binding name to object

a = "first"
b = "first"
 
 
# Returns the actual location
# where the variable is stored
print(id(a))
 
# Returns the actual location
# where the variable is stored
print(id(b))
 
# Returns true if both the variables
# are stored in same location
print(a is b)

# Mutable and unmutable

a = [10, 20, 30]
b = [10, 20, 30]
 
# return the location
# where the variable
# is stored
print(id(a))
 
# return the location
# where the variable
# is stored
print(id(b))
 
# returns false if the
# location is not same
print(a is b)