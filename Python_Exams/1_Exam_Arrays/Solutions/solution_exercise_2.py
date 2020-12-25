list_variable = []

i=0
while (i < 5):
  element = input("Add contact name: ")
  if element in list_variable:
    print("Your contact is already in your list.")
  else:
    list_variable.append(element)
    i=i+1

print("You list is: " + str(list_variable))

i=0
longest_word = list_variable[0]

while (i < len(list_variable)):
  if len(list_variable[i]) > len(longest_word):
    longest_word = list_variable[i]
  i = i + 1

print("Your contact with the longest name is: " + str(longest_word))