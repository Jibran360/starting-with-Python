greeting = 'Good Morning, '
name = "jibran"
print(type(name))
print(greeting + name)

# Concatinating two strings
c = greeting + name
print(c)

# Assigning Index of string
name = "jibran"
print(name[0])
#name[3] = "d"          #--> Does not work

# String Slicing
name = "Jibran"
print(name[0:3])       # String into pieces
print(name[ :4])       # is same as name[0 : 4]
print(name[1: ])       # is same as name[1 : 5] --> length of the string
print(name[-4:-1])     # is same as name[1 : 4]

d = name[3 : 6]

# Slicing with skip value
name = "Jibran"
d = name[2:5:2]         # skip every second value
print(d)