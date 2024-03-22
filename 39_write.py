# write and append modes!
''' 'w' for write mode, it writes any word given by user in the .txt file.  and every time when we change the word write
mode will change the whole .txt file'''
# 'a' append mode will add the given change at the end of the already existing .txt file 

f = open('another.txt', 'w')
f = open('another.txt', 'a')
f.write("This is nice\n")
f.write("this is good")
f.close()