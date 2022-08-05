x = int(input("Upper Limit:"))
list = []
primes = [2]
for i in range(x-1):
  list.append(i+2)
print(list)
for j in range(0, len(list)):
  prime = True
  for m in range(0, len(primes)):
    if(list[j]%primes[m] == 0 ):
      prime = False
      break
  if (prime == True):
    primes.append(list[j])
print(primes)
