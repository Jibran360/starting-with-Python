#PR-1
# num = int(input("Enter the number:"))
# for i in range(1, 11):
    # print(str(num) + " X " + str(i) + "=" + str(num*i))
    # print(f"{num}X{i}={num*i}")                                   # f strings


#PR-2
# l1 = ["ali", "saad", "hamza", "saif"]

# for name in l1:
    # if name.startswith("s"):
        # print("Hello " + name)


#PR-3
# num = int(input("Enter the number: "))
# i = 1
# while i<=10:
    #  print(str(num) + " X " + str(i) + "=" + str(i*num))
    #  i = i + 1


#PR-4
# num = int(input("Enter the number: "))

# prime = True
# for i in range(2, num):
#     if(num%i == 0):
#         prime = False
#         break
# if prime:
#         print("This number is prime")
# else:
#     print("This number is not prime")


#PR-5
# num = int(input("Entre the number: "))
# sum = 0
# while num>0:
#     sum += num
#     num -= 1
#     print("The sum is", sum)



#PR-6
# n! = 1 X 2 X 3 X 4 X ..... X n     -> factorial
# 5! = 1 X 2 X 3 X 4 X 5

# num = int(input("Enter the number: "))
# factorial = 1
# for i in range(1, num+1):
#     factorial = factorial * i

# print(f"The factorial of this number is {factorial}")


#PR-7
# n = 3
# for i in range(3):
    # print(" " * (n-i-1), end="")
    # print("*" * (2*i+1), end="")
    # print(" " * (n-i-1))



#PR-8
n = 4

for i in range(4):
    print("*" * (i+1))



#PR-10
# num = int(input("Enter the number:"))
# limit = int(input("Enter the ending: "))
# for i in range(limit, 0, -1):
    # print(str(num) + " X " + str(i) + "=" + str(i*num))
    # print(f"{num}X{i}={num*i}")

# PR-9
# print("* * * *")
# print("*     *")
# print("* * * *")

# n = 3
# for i in range(3):
#     print(" " * (n), end="")
#     print("*" * (i), end="")
#     print(" " * (n))