number = int(input("What number to factor:"))
  list = []
  for i in range(1, number + 1):
    if((number / i)%1 == 0):
      list.append(i)
  print('the factors of', number, 'are', list)