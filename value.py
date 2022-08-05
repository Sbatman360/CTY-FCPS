class Value:
  def __init__(self, a, b):
    self.a = a
    self.b = b
  def add(self):
    return(self.a + self.b)
  def tuple(self):
    c = (self.a, self.b)
    return c

def double_char(str):
  str.split()
  print(str)
  new = []
  for i in range(0, len(str)):
    new.append(str[i])
    new.append(str[i])
  return new
def b10to2(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal*2 + int(digit)
print(b10to2('101010'))