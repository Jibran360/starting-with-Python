# from operator import index


# Properties of sets:
# 1. Sets are unordered  -> Elements order does'nt matter
# 2. Sets are unindexed  -> cannot access elements by index
# 3. There is no way to change items in sets. 
# 4. Sets cannot duplicate vlaues.


# a = {1, 2, 3, 4, 1}        # sets can't hold repetitive elements
# print(a)
# print(type(a))



# EMPTY SET

# This syntax will create an empty dictionary and not an empty set
# a = {}
# print(type(a))

# An empty set can be created by using the below syntax

# Creatig an empty set
b = set()
print(type(b))

# Adding values to an empty set
b.add(4)
b.add(5)
# b.add(5)           # Adding a value repeatedly does not changes a set
# b.add(5)
b.add((4, 3, 5))     # tuple can be added in set

# hashable data type can't be added in set
# b.add([4, 3, 5])     # list can't be added in set(hashable)

# Accessing elements 
# b.add({4, 5})        # dictionary can't be added in set because it is hashable
print(b)

# Prints lenght of the set
# print(len(b))         # prints the length of this set

# Removal of item
# b.remove(5)           # removes 5 form set b
# b.remove(15)          # throws an error while trying to remove 15(which is not present in the set)
# print(b)

# print(b.pop())         # Removes any random value from the set
# print(b)

# print(b.clear())
# print(b)

