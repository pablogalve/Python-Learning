num1 = int(input("Write a number."))
num2 = int(input("Write another number."))

i=1
j=1
div1=0
div2=0

while (i < num1):
  if (num1 % i == 0):
    div1=(i + div1)
  i+=1

while (j < num2):
  if (num2 % j == 0):
    div2=(j + div2)
  j+=1

if (div1 == num2) and (div2 == num1):
  print("Both numbers are friends.")
else:
  print("Numbers are not friends.")