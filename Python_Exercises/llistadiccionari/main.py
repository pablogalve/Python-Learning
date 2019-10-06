print("Menú de la pizzeria:Cantinapetit")
print("1- Afegir una pizza amb ingredients")
print("2- Eliminar ingredients de una pizza")
print("3- Eliminar una pizza")
print("4- Llistar les pizzas")
print("5- Llistar les pizzas que tenguin un ingredient determinat")
print("6- Surt del programa")
menu={}
preus=menu.values()
opcio=int(input("Introdueix una opció: "))
while (opcio!=6):
  if (opcio==1):
    pizza=input("Inrodueix una pizza: ")
    num=int(input("Digues un num pels ingredients de la pizza"))
    i=0
    llista=[]
   
    while (i<num):
      ingredient=input("Introdueix un ingredient per la pizza")
      llista.append(ingredient) 
      i=i+1
    preu=input("Introdueix es seu preu: ")
    menu[pizza]=preu
  if (opcio==2):
    piz=input("Digues la pizza de la cual vols eliminar ingredients")
    num2=int(input("Digues quants elements vols eliminar"))
    i=0
    while (i<=num2):
      if (piz in menu):
        ingre=input("Quin ingredient vols eliminar")
        if (ingre in llista):
            llista.remove(ingre)
      i=i+1
    print(piz)
  opcio=int(input("Introdueix una opció: "))    
print (menu)