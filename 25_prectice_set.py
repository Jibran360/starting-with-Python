# PR_1
# num1 = int(input("Enter 1st number: "))
# num2 = int(input("Enter 2nd number: "))
# num3 = int(input("Enter 3rd number: "))
# num4 = int(input("Enter 4th number: "))
# 
# if(num1>num4):
#     f1 = num1
# else:
#     f1 = num4
# 
# if(num2>num3):
#     f2 = num2
# else:
#     f2 = num3
# 
# if(f1>f2):
#     print(str(f1) + " is greatest")
# else:
#     print(str(f2) + " is greatese")


# PR_2
# sub1 = int(input("Enter first subject marks\n "))
# sub2 = int(input("Enter second subject marks\n "))
# sub3 = int(input("Enter third subject marks\n "))

# if(sub1<33 or sub2<33 or sub3<33):
#     print("You are fail because you have less than 33% in one of the subjects")

# elif(sub1+sub2+sub3)/3 <40:
#     print("You are fail due to total percentage less than 40 ")
# else:
#     print("You are Passed, Congratulations!")


# PR_3
text = input("Enter the text\n")
spam = False
if("make alot of money" in text):
    spam = True
elif("buy now" in text):
    spam = True
elif("click this" in text):
    spam = True
elif("subscribe this" in text):
    spam = True
else:
    spam = False
if(spam):
    print("This text is spam")
else:
    print("This is not a spam")


#PR_4
# name = input("Enter char: ")
# print(len(name))
# if(len(name)<10):
#     print("It contains less char")
# else:
#     print("It contains equal or more char")


#PR_5
# name = ["hamza, ali, ahad, saad, dani"]
# check = input("Enter the name to check\n")

# if check in name:
#     print("Your name is present in the list")
# else:
#     print("Your name is not present in the list")


#PR_6
# marks = int(input("Enter your marks\n"))

# if marks>=90:
#     grade = "Ex"
# elif marks>=80:
#     grade = "A"
# elif marks>=70:
#     grade = "B"
# elif marks>=60:
#     grade = "C"
# elif marks>=50:
#     grade = "D"
# else:
#     grade = "F"

# print("Your grade is " + grade)


#PR_7
# post = input("Enter a post: ")

# if 'saad' or 'SAAD' in post:
#     print("Yes! it is present")
# else:
#     print("No! it is not there")

