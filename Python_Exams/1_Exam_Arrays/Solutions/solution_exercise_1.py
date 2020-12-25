num = int(input("How many elements do you want to include in the list?"))

i = 0
list_variable = []

while (i < num):
  element=input("Add a number to the list: ")
  list_variable.append(element)
  i=i+1

print("You list is: " + str(list_variable))