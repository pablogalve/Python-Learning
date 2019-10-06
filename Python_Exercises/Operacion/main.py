num1=int(input("Digues un numero"))
num2=int(input("Digues un altre numero"))
oper=str(input("Ara digues una operacio"))
if (oper=="s"):
  print(num1+num2)
if (oper=="r"):
  print(num1-num2)
if (oper=="m"):
  print(num1*num2)
if(oper=="d"):
  print(num1/num2)
if (oper=="e"):
  print(num1**num2)