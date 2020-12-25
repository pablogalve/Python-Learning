frase=str(input("Write a sentence and I'll give you back the letters that are in even positions."))

i=0

frase=frase.replace(' ','') 
leng=len(frase)

while (i<=leng):
  if (i%2!=0):
    print(frase[i])
  i+=1