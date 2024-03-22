# from msilib.schema import Property
# from typing import MutableMapping, OrderedDict


# Propertyies of Dictionary:
# 1. It is un-Ordered
# 2. It is Mutable(can change)
# 3. It can not contain duplicate keys 
# 4. It is Indexed





myDict = {
          "Fast" : "In a Quick Manner",          # String
          "Ali" : "A Coder",                     
          "Marks" : [1, 2, 4],                    # list
          "anotherDict" : { "Ali": "Player" }
        }

# print(myDict['Fast'])
# print(myDict['Ali'])
# myDict['Marks'] = [45, 33]
# print(myDict['Marks'])
print(myDict['anotherDict'],['Ali'])


