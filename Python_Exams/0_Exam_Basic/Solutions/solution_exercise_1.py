num=int(input("Write a number and I'll return all its dividers."))

i=1

while (i <= num):
  if (num % i == 0):
    print(str(i) + " is a divider of you number.")
  i+=1