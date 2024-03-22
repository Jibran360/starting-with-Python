# Use open function to read the content of a file!

# f = open('sample.txt', 'r')
f = open('heart.txt')            # by default the mode is r(read)
# data = f.read()                # read its contents

data = f.read(26)                # reads first 6 characters from the file
print(data)                      # print its contents
f.close()                        # close the file. (its mendatory to close a file at the end of the program)