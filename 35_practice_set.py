#PR-1
# def maximum(num1, num2, num3):
#     if(num1>num2):
#         if(num1>num3):
#             return num1
#         else:
#             return num3
#     else:
#         if(num2>num3):
#             return num2
#         else:
#             return num3
# 
# m = maximum(13, 45, 66)
# print("The value of the maximum is " + str(m))


#PR-2
# def farh(cel):
#     return (cel *(9/5)) + 32

# c = 0
# f = farh(c)
# print("Fahrenhite Temperature is " + str(f))


#PR-3
# print("Hello", end=" ")
# print("How", end=" ")
# print("are", end=" ")
# print("you?", end=" ")       # [end=""] to prevent a python print() function to print a new line at the end.


#PR-4
# def factorial_iter(n):
#     sum = 1
#     for i in range(n):
#         sum = sum + (i-1)
#     return sum

# def factorial_recursive(n):
#     if n == 1 or n == 0:
#         return 1
#     return n + factorial_recursive(n-1)

# f = factorial_recursive(10)
# print(f)


#PR-5
# n = 9
# for i in range(n):
#     print("*" * (n-i))      # print * n-i times.


#PR-6
# def inch(cm):
#     return (cm *(2.54))
# c = 9
# i = inch(c)
# print("cm is " + str(i))


#PR-7
# what is strip and what is its use?
# this = "    Saad is good    "
# print(this)
# print(this.strip())             # removes extra spaces.

# def remove_and_split(string, word):
#     newStr = string.replace(word, "")
#     return newStr.strip()

# this = "    Saad is good    "
# print(this)
# n = remove_and_split(this, "Saad")
# print(n)


#PR-8
def table(num):
    return (str(num) + " X " + str(i) + "=" + str(num*i))

num = int(input("Enter the number: "))

print("Multiplication Table of", num)
for i in range(1, 11):
   # print(num,"X",i,"=",num * i)
   print(f"{num}X{i}={num*i}")
