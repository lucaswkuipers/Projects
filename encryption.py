#--Function Defining--#
def encrypt(phrase_input, correspondents):
  #Phrase input is string and correspondents is a dictionary matching symbols to each other
  phrase_input = phrase_input.lower()

  #Get it's length (size_input)
  size_input = len(phrase_input)
  
  #Create copy of string as list
  phrase_list = list(phrase_input)
  
  #Create copy of list
  copy_list = phrase_list[:]

  #Loop through dictionary
  for letter, correspondent in correspondents.items():
    from_letter = letter
    to_letter = correspondent
    #Find given letter, get its ocurrences (index of positions in the list)
    count = -1
    ocurrences = []
    for letter in phrase_input:
      count = count + 1 #Index of current element
      if letter == from_letter:
        ocurrences.append(count)
    # print('Ocurrences of %s:' % (from_letter), ocurrences)


    #Fill new list with the correspondent of the given letter
    for position in ocurrences:
      copy_list[position] = to_letter
    # print('After changing %s to %s:' % (from_letter, to_letter), copy_list)
  final_message = ''.join(copy_list)
  final_message = final_message.split()
  last_list = []
  for word in final_message:
    new_word = word.capitalize()
    last_list.append(new_word)
  message = ' '.join(last_list)
  return message
#----#

#--Testing Function--#
mensagem = 'Socorro, estamos em perigo!'
chave = {'z': 'p', 'p': 'z', 'e': 'o', 'o': 'e', 'n': 'l', 'l': 'n', 'i': 'a', 'a': 'i', 't': 'r', 'r': 't'}
criptografada = encrypt(mensagem, chave)
decifrada = encrypt(criptografada, chave)

print(mensagem)
print(criptografada)
print(decifrada)
#----#