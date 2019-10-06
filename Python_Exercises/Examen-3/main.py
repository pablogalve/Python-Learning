frase=str(input("Digues una frase i et dire les lletres que es troben en la posicio par d'aquesta mateixa com si no hi hagues espais en blanc"))
i=0
frase=frase.replace(' ','') 
leng=len(frase)
while (i<=leng):
  if (i%2!=0):
    print(frase[i])
  i+=1