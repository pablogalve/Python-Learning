num=int(input("Set array size: "))

i = 0
variable_list = []

while (i < num):
  word = input("Add a new word to the list: ")
  variable_list.append(word) 
  i = i + 1
  
print (variable_list)

search = input("Introduce a name to search it in the list: ")
variable_list.index(search)
print(search)