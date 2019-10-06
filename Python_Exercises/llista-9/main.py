num=int(input("Quantes paraules vols"))
llista=[]
i=0
#procediment per incorporar paraules a la llista
while i<num:
  paraula=input("Digues una paraula:")
  llista.append(paraula)
  i=i+1
print(llista)
#hem de tornar a recòrrer la llista i veure quines paraules estàn repetides.
i=0
while i<num:
  encontrado=True
  j=0
  elem=llista.count(llista[i])
  # per cada paraula de la llista hem de comparar-les amb les altres, per veure quina hem d'esborrar.
  while j<num:
# si la paraula està repetida hem de mirar on està la primera i obviar-la per esborrar les altres   
    if elem>1:
      paraula=llista[i]
      if llista[j]==paraula:
        if encontrado == True:
          encontrado=False
        else:
          llista.pop(j)
          num=num-1
    j=j+1
  i=i+1  

print("La nova llista sense repeticions es " +str(llista))