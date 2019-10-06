cad=str(input("digues una frase i et contare les vocals"))
cad=cad.replace(' ','')
contar_vocales=0
for taula in cad:
  if taula == 'a' or taula == 'e' or taula == 'i' or taula =='o' or taula == 'u' or taula == 'A' or taula == 'E' or taula == 'I' or taula =='O' or taula == 'U':
    contar_vocales+=1
print ("La frase tiene " + str(contar_vocales) +" vocales")