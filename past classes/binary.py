
x = int(input('number: '))
dec = x
binary = ''
while x > 0:
  carry = str(x%2)
  x = int(x / 2)
  binary = binary + carry
print(binary)
