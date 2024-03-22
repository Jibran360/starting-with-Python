from audioop import mul


myDict = {
          "fast" : "In a Quick Manner",          # String
          "ali" : "A Coder",                     
          "marks" : [1, 2, 4],                    # list
          "anotherDict" : { "Ali": "Player" },
          1 : 2
        }


# Dintionary methods

# print(myDict.keys())
# print(list(myDict.keys()))

# print(type(myDict.keys()))    # prints the keys of the dictionary

# print(myDict.values())
# print(myDict.items())         # print the key, values for all contents of the dictionary

# print(myDict)
# updateDict = {                  # update new items in the dictionary
#     "Lovish" : "Friend",
#     "ali" : "A Dancer"
# }
# myDict.update(updateDict)       # update the dictionary by adding key-value pairs from updateDict
# print(myDict)

# print(myDict.get("ali"))         # prints value associated with key "ali"
# print(myDict["ali"])           # prints value associated with key "ali"

# The difference between .get and [] syntax in Dictionaries?
# print(myDict.get("ali2"))         # returns none as ali2 is not present in the dictionary
# print(myDict["ali2"])             # throws an error as ali2 is not present in the dictionary
