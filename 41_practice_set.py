# PR-1
# f = open('poems.txt')
# t = f.read()
# if 'twinkle' in t:
#     print("Twinkle is present")
# else:
#     print("Twinkle is not present")
# f.close()

#PR-2
# ef game():
#    return 90
# core = game()
# ith open("highscore.txt") as f:
#    highscore = int(f.read())
# f highscore<score:
#    with open("highscore.txt", "w") as f:
#        f.wite(str(score))
# core = game()
# ith open("highscore.txt") as f:
#    highScoreStr = f.read()
# f highScoreStr=='':
#    with open("highscore.txt", "w") as f:
#        f.wite(str(score))
# lif int(highScoreStr)<score:
#    with open("highscore.txt", "w") as f:
#        f.wite(str(score))


#PR-3
# for i in range(2, 21):
#     with open(f"tables/Multiplication_table_of_{i}.txt", 'w') as f:
#         for j in range(1, 11):
#             f.write(f"{i}X{j}={i*j}\n")
#             # if j!=10:
#                 # f.write('\n')
#     break


#PR-4
# with open("sample.txt") as f:
#     content = f.read()
# content = content.replace("112233", "$%^@$^#")
# with open("sample.txt", "w") as f:
#     f.write(content)


#PR-5
# words = ["donkey", "kaddu", "bc"]

# with open("sample.txt") as f:
#     content = f.read()
# for word in words:
#     content = content.replace(word, "$%^@$^#")

# with open("sample.txt", "w") as f:
#     f.write(content)


#PR-6
# with open("log.txt") as f:
#     content = f.read()

# if 'python' or 'PYTHON' in content:
#     print("Yes python is present")
# else:
#     print("Not present")


#PR-7
# content = True
# i = 1
# with open("log.txt") as f:
#     while content:
#         content = f.readline()
#         if 'python' in content.lower():
#             print(content)
#             print(f"Yes python is present on line {i}")
#         # else:
#         #     print("Not present")
#         i+=1


#PR-8
# with open("heart.txt") as f:
#     content = f.read()

# with open("copy.txt", 'w') as f:
#     f.write(content)


#pr-9
# Files are identical or not 
# file1 = "copy.txt"
# file2 = "this.txt"
# with open(file1) as f:
#     f1 = f.read()
# with open(file2) as f:
#     f2 = f.read()
# if f1 == f2:
#     print("Files are identical")
# else:
#     print("Files are not identical")


#PR-10
# To wipe all content in a file 
# filename = "this.txt"
# with open(filename, 'w') as f:
#     f.write("")


#PR-11
import os

oldname = "this.txt"
newname = "renamed_by_python.txt"
with open(oldname) as f:
    content = f.read()

with open(newname, "w") as f:
    f.write(content)

os.remove(oldname)