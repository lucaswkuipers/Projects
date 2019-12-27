#Idea: Computer asks user for his age and return a category he fits

age = input("Hi! Please type in your age ") #2 and #3
age = int(age)

if age < 0: #4
    category = "Liar"
elif age <= 13:
    category = "Child"
elif age <= 17:
    category = "Teenager"
elif age <= 24:
    category = "Young Adult"
elif age <= 64:
    category = "Adult"
elif age <= 120:
    category = "Elder"
else:
    category = "Dead"

print("You are " + category) #1
