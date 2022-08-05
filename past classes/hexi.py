
def hexadecimal():
  letters = ['A', 'B', 'C', 'D', 'E', 'F']

  x = dec
  hexa = ''
  while x > 0:
    carry = str(x%16)
    x = int(x / 16)
    if int(carry) >= 10:
      carry = letters[int(carry)-10]
    hexa += carry

  return (hexa[::-1])

