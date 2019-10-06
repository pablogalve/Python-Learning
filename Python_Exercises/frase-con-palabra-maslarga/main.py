frase=str(input("Digues una frase y et dire la paraula mes llarga d'aquesta"))
leng=len(frase)
cont=0
i=0
maxim=0
while (i<=leng-1):
  if frase[i]!=" ":
    cont=cont+1
  if frase[i]==" " or i==leng-1:
    if cont>maxim:
      maxim=cont
      cont=0
  i=i+1
      
print("La paraula més llarga és de " + str(maxim) + " lletres")
