def hexadecimal(input, base):
  letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', "K", "L", 'M', 'N', "O", 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', "Z"]
  base = int(base)
  x = int(dec)
  hexa = ''
  while x > 0:
    carry = str(x%base)
    x = int(x / base)
    if int(carry) >= 10:
      carry = letters[int(carry)-10]
    hexa += carry
  return (hexa[::-1])
base = 100
while base > 36:
  dec =  input("decimal: ")
  base = int(input("base: "))
  if base > 36:
    print("Please use base 36 or under")
  elif(base != int or dec != int):
    print('Error: decimal or base not integers')
  
print("Your number is:", hexadecimal(dec, base))