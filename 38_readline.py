f = open('sample.txt')        

# Read first line
data = f.readline()               
print(data)   

# Read sacond line
data = f.readline()               
print(data)       

#Read third line
data = f.readline()               
print(data) 

# Read fourth line...  and so on..
data = f.readline()               
print(data) 
f.close()