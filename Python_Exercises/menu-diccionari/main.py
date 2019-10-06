buscar=bool
print("Menú del programa")
print("1- Afegir un plat i es seu preu")
print("2- Buscar un plat")
print("3- Eliminar un plat")
print("4- Mostrar els plats")
print("5- Mostrar els preus")
print("6- Mostrar el plat més car")
print("7- Mostrar el plat més barat")
print("8- Surt del programa")
opcio=int(input("Introdueix una opció: "))
menu={}
preus=menu.values()
while (opcio!=8):
  if (opcio==1): # instroduim un plat
    plat=input("Introdueix el nom des plat:")
    preu=input("Introdueix es seu preu: ")
    menu[plat]=preu
  opcio=int(input("Introdueix una opció: "))
  if (opcio==2):
    nom=input("Introdueix un plat a buscar i et dire el preu")
    if (nom in menu):
      buscar=True
    else:
      buscar=False
    if (buscar==True):
      print("El plat buscat " + str(nom) + ", esta en el menu i seu preu es " + menu.get(nom))
    else:
      print("El plat no esta")
  if (opcio==3):
    eliminar=input("Digues un plat a eliminar")
    if eliminar in menu:
      del menu[eliminar]
      print(menu)
    else:
      print("el plat que vols eliminar no es existeix")
  if (opcio==4):
    plats=menu.keys()
    print("Els plats són: ")
    for plat in plats:
      print (plat)
  if (opcio==5):
    print("Els preus son: ")
    for preu in preus:
      print(preu)
  if (opcio==6):
    preus=menu.values()
    maxim=0
    for preu in preus:
      if int(preu)>int(maxim):
        maxim=preu
    print("El plat amb el preu més elevat val " +str(maxim))
  if (opcio==7):
    preus=menu.values()
    minim=999999
    for preu in preus:
      if int(preu)<int(minim):
        minim=preu
    print("El plat amb el preu més barat val " + str(minim))
        
print("El menu final és " + str(menu))
print ("Adeu")