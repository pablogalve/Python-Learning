print("...CIUDADES...")
print("1-Afegir un element a la llista")
print("2-Esborrar un element de la llista")
print("3-Buscar un element de la llista")
print("4-Surt del programa")
llista=[]
i=0
opcio=int(input("Digues una opció"))
while (opcio!=4):
  if (opcio==1):
    element=input("Digues la ciutat que vols afegir")
    llista.append(element)
    print(llista)
  if (opcio==2):
    eliminar=input("Digues la ciutat que vols eliminar de la llista")
    if eliminar in llista:
      llista.remove(eliminar)
    else:
      print("L'element buscat per a eliminar no esta a la llista")
    print(llista)
  if (opcio==3):
    cont=0
    buscar=input("Digues un element a buscar en la llista")
    if buscar in llista:
      cont=cont+1
      print("La ciutat buscada surt " +str(cont) + " vegada/es")
    else:
        print("La paraula buscada no esta a la llista")
  opcio=int(input("Digues una opció"))
print("La llista final es " + str(llista))
