sentence = input("Write a sentence: ")
print()
long = len(sentence)
reverse=""

for i in range(long):
  reverse = reverse + sentence[long-1]
  long = long-1

print("Your sentence in reverse order is: " + str(reverse))