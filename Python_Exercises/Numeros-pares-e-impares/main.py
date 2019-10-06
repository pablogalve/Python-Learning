num=int(input("digues numeros, et dire si son pars o impars, per a que acabi la cadena posa un cero"))
par=0
impar=0
while num!=0:
    if(num%2)==0:
        par=par+1
    else:
        impar=impar+1
    num=int(input("digues un altre numero"))
print("Hi has postat " + str(par) + " numeros pars " + "i " + str(impar) + " numeros impars")