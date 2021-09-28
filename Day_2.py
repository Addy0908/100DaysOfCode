#LOVE CALCULATOR
print("Welcome to the love calculator")
Name1= input("What is your name:- ")
Name2= input("What is your partners name:- ")
combined_string= Name1 + Name2
a = combined_string.lower() #tolower
t=a.count("t")
u=a.count("u")
r=a.count("r")
e=a.count("e")
true=t + u + r + e

l=a.count("l")
o=a.count("o")
v=a.count("v")
e=a.count("e")
Love = l + o + v + e + e

love_score = int(str(true) + str(Love))

if(love_score <10) or (love_score > 90):
    print(f"Yor love score is {love_score} , you go together like coke and mentos")
elif (love_score >=40) and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")




