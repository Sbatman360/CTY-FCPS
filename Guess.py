print("Think of a number from 0 to 1022")
high = 1022
low = 0
mid = 511
x = ''
while(x != 'X' and x != 'x'):
  mid = round((high + low)/2, 0)
  print('Is it', mid, "?")
  x = input("answer with H(higher), L(lower) or X(the number):")
  if x == 'H' or x == 'h':
    low = mid
  elif x == 'L' or x == 'l':
    high = mid
print("Horray your number is:", mid)
