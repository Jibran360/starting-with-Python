# PR-1
# greeting = input("Enter greetings: " )
# name = input("Enter name: ")
# print(greeting + name)
# print("Good Afternoon, " + name)


# PR-2
#letter = '''Dear <|NAME|>,
#You are selected!

#Date: <|DATE|>
'''
name = input("Enter Your Name:\n")
date = input("Enter Date:\n")
greet = "Thanks\n"
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)
print(greet) '''


# PR-3
# story = "once upon a time there was a youtuber who  upload python course with notes"
# doubleSpaces = story.find("  ")
# doubleSpaces = story.replace(" ", "  ")
# print(doubleSpaces)


# PR-4
letter = "Dear Ali, this Python course is nice! Thanks!"
print(letter)
formatted_letter = "Dear Ali,\n\t this Python course is nice!\nThanks!"
print(formatted_letter)