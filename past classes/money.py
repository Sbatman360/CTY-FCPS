value = int(input("enter a value to HOTPO: "))
initialvalue = value
steps = 0
while value != 1:
  if value % 2 == 0:
    value /= 2
    steps +=1
  else:
    value = value*3 -1
    steps +=1
print('A HOTPO of',initialvalue, 'finishes in',steps,'steps.')