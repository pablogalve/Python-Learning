print("...CITIES...")
print("1-Add an element to the llist.")
print("2-Remove an element from the list.")
print("3-Find an element in the list.")
print("4-Exit the program")

list_variable = []
i = 0
chosen_option = int(input("Choose an option: "))

while (chosen_option != 4):
  if (chosen_option == 1):
    element = input("What city do you want to add to the list? ")
    list_variable.append(element)
    print(list_variable)
  if (chosen_option == 2):
    erase = input("What city do you want to remove from the list? ")
    if erase in list_variable:
      list_variable.remove(erase)
    else:
      print("Your element is not on the list.")
    print(list_variable)
  if (chosen_option == 3):
    cont = 0
    buscar=input("What city do you want to find in the list? ")
    if buscar in list_variable:
      cont = cont + 1
      print("Your city appears " + str(cont) + " times on the list.")
    else:
        print("Your word is not on the list.")
  chosen_option=int(input("Choose another option: "))
print("The final list is: " + str(list_variable))