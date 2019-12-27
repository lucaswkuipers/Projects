# String least spacing
# Given a big string and a list of smaller strings, find the minimum amount of spaces that must be inserted between characters of the string in such way that it becomes composed only of elements from the list of smaller strings. (and which are the respective elements used). from a given list

import itertools
import numpy as np

# Given large string
big_string = '3141592653589793238462643383279'
big_string_len = len(big_string)

# Given list of available strings
small_strings = ['3', '314', '49', '9001', '15926535897', '14', '9323', '8462643383279', '4', '793', '3141592653589793238462643383278', '314159265358979','3238462643383279']

# Removing non ocurring elements
small_strings = [x for x in small_strings if x in big_string]

# Finding combinations that match the length of the long number
possibilites = list()
for k in range(1, len(small_strings)):
  c = list(itertools.combinations(small_strings, k))
  combinations =  [x for x in c if sum(len(i) for i in x) == big_string_len]
  possibilites.extend(combinations)

# Permutating tuples inside the list to see if they match the big_string. If so, store the permutated tuple in a list
matches = list()
for tup in possibilites:
  p = list(itertools.permutations(tup))
  permutations = [x for x in p if ''.join(x) == big_string]
  matches.extend(permutations)

# Binding the matches with their lengths in a dictionary
sizes = dict()
for tup in matches:
  sizes[tup] = len(tup)

# Finding the optimal solution (minimal length, and where it occurres)
min_key = min(sizes, key=sizes.get)
min_val = sizes[min_key]

# Give the optimal solution
print('Best solution is', ' '.join(min_key), 'with', min_val - 1, 'space(s)')
