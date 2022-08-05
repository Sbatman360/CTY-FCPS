locker = []

for i in range(100):
  locker.append('1')

for m in range(2,101):
  for j in range(100):
    if j%m == 0:
      if locker[j-1] == '1':
        locker[j-1] = '0'
      else:
        locker[j-1] = '1'
  
print(locker)