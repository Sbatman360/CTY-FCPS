list = [1,4,6,7,9,15,16,18,22,25,26,30]
odd = 0
even = 0
for i in range(0, len(list)):
  if list[i] %2 == 1:
    odd +=1
  else:
    even+=1
print(even, 'even numbers and', odd, "odd numbers")