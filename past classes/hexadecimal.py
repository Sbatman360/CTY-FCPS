import math

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', "K", "L", 'M', 'N', "O", 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', "Z"]
decimal = int(input("decimal number input:"))
i = 0
copy = int(decimal)
#find maxdigit
s = int(input('base: '))

while(copy > s):
  decimal = decimal / s**i
  i+=1
maxdec = str(i)
hexadecimal = ''
for j in range(i):
  digit = str(decimal/s**(i-j))
  decimal = decimal % s**(i-j)
  hexadecimal += digit

print(hexadecimal)