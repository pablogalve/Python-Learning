i=0
llista=[]
while (i<5):
  element=input("Digues un contacte que vols afegir")
  if element in llista:
    print("Aquest contacte ja es a la llista, no el pots afegir")
  else:
    llista.append(element)
    i=i+1
print(llista)
i=0
major=llista[0]
while (i<len(llista)):
  if llista[i]>major:
    major=llista[i]
  i=i+1
print(major)