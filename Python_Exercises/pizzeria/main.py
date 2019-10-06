menu={}
print("Menu de la pizzeria")
print("1.- Afegir una pizza amb ingredients")
print("2.- Eliminar ingredients de una pizza")
print("3.- Eliminar una pizza")
print("4.- Llistar les pizzas")
print("5- Eliminar un ingredient de totes les pizzes")
print("6.- Llistar les pizzas que tenguin un ingredient determinat")
print("7.- Sortir del programa")
opcio=int(input("Introdueix quina opcio vols fer: "))
pizza_ingred=menu.items()
buscar=bool
while opcio!=7 :
  if opcio==1:
    pizza=input("Introdueix una pizza")
    
    num=int(input("Digues quants ingredients vols afegir a la pizza: "))
    i=0
    llista=[]
    while i<num:
      ingredient=input("Introdueix un ingredient per a la pizza")
      llista.append(ingredient)
      i=i+1
    print(llista)
    menu[pizza]=llista
    print(menu)
    
  if opcio==2:
    print(menu)
    piz=input("Digues de quina pizza vols eliminar els ingredients: ")
    num2= int(input("Digues quants elements de la pizza vols eliminar: "))
    j=0
    while j<num2:
      print(menu)
      print(pizza_ingred)
      for pizza_b, ingre_b in pizza_ingred:
        ingredient=input("Digues quin ingredient vols eliminar")
        llista_ingr=[]
        llista_ingr=ingre_b
        print(llista_ingr)
        if ingredient in llista_ingr:
          llista.remove(ingredient)
          print(llista)
      j=j+1
      
  if opcio==3:
    eliminar=input("Introduieix una pizza que vols eliminar")
    if eliminar in menu:
      del (menu[eliminar])
    print(menu)
    
  if opcio==4:
    llista=menu.keys()
    print(llista)
    
  if opcio==5:
    eliminar2=input("Digues quin ingredient vols eliminar de les pizzes")
    for pizza, ingr in pizza_ingred:
      llistaingre=ingr
      if eliminar2 in llistaingre:
        llistaingre.remove(eliminar2)
        print("El nou menu es " + str(menu))
      else:
        print("L'ingredient que vols eliminar no esta a cap pizza")
        
  if opcio==6:
    ingre=input("Digues un ingredient a buscar")
    for pizza, llistaingre in pizza_ingred:
      ingredients=[]
      ingredients=llistaingre
      if ingre in ingredients:
        print("El ingredient esta a la pizzes: " +str(pizza))
        
  opcio=int(input("Introduieix quina opcio vols fer: "))
print("Has sortit del programa")
