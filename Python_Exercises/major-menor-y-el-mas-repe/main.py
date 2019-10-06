numer=input("Digues una serie de numeros separats per espai i et dire el numero mes gran, el mes petit i el que mes es repeteix d'aquesta")
leng=len(numer)
repe=0
cont=0
petit=0
gros=0
i=0
while (i<leng-1):
  if numer[i]!=" ":
    cont+=1
  

  i=i+1
  
  
print("El numero mes gran es el " + str(maxim) + " el mes petit es " + str(minim)+ " i el que mes es repeteix es el " + str(repe))