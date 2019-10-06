num=int(input("Digues un numero i et tornare els divisors de aquest"))
i=1
while (i<=num):
  if (num%i==0):
    print(str(i) + " Aquest num es divisor del numero")
  i+=1