 #Idea: Random Name Generator: Given a list of first and last names, sort it alphabetically. Give the lists length and their first and last name. Choose how many last names the name must contain and if they can be repeated.

import random
valid = False
ans = '0'

#### Importing First Names  ####
first_names = list()
with open('C:\Projects\name_generator\first_names.txt', 'r') as f:
  for line in f:
    first_names.append(line)
  first_names = [line.rstrip('\n') for line in open('C:\Projects\name_generator\first_names.txt')]

#### Importing Last Names ####
last_names = list()
with open('C:\Projects\name_generator\last_names.txt', 'r') as f:
    text = f.read()
    text = text.split()

for element in text:
  if element.isalpha():
    last_names.append(element)

####  FIRST NAMES ####
first_names.sort() #Organizing Aplhabetically
num_first_names = len(first_names)
print("There are " + str(num_first_names) + " first names possibilities")

####  LAST NAMES  ####
last_names.sort() #Organizing Aplhabetically
num_last_names = len(last_names)
print("There are " + str(num_last_names) + " last names possibilities")

#### Capitalzie List ####
first_names = [name.capitalize() for name in first_names]
last_names = [name.capitalize() for name in last_names]

####  NAME SIZE ####
while valid == False:
  n = int(input("How many surnames must your name contain? \n"))
  if not int(n) > 0:
    print('Please type a valid natural number (Ex: 1, 2, ..., 1000)')
  else:
    valid = True
    if n >= num_last_names:
      can_repeat = True
    else:
      if n == 1:
        can_repeat = False
      else:
        while ans != 'Y' and ans != 'N':
          ans = input("Could the names repeat? (Y/N) \n")
          if ans == 'Y':
            can_repeat = True
          elif ans == 'N':
            can_repeat = False
          else:
            print("Please type Y (for yes) or N (for no) ")

####  Generating Name ####

#First Name
first_name = first_names[random.randint(0,num_first_names-1)] #First name

#Last Name
last_name = ''
if can_repeat:
  for i in range(n):
    last_name = last_name + ' ' + last_names[random.randint(0,num_last_names-1)]
else:
  used_names = []
  i = 0
  while i < n:
    new_name = last_names[random.randint(0,num_last_names-1)]
    if not new_name in used_names:
      used_names.append(new_name)
      last_name = last_name + ' ' + new_name
      i += 1


name = first_name + last_name

#### Output ####
print(name)
