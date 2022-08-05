import math
def pytheorum(x, y):
  z = (x**2+y**2)**0.5
  return(z)

def area(x, y):
  return (x*y)/2

def palindrome(str1):
  str2 = str1[::-1]
  if(str2 == str1):
    return True
  else:
    return False

def factorial(x):
  for i in range(1, x+1):
    x = x * i
  return x


def fib():
  x = int(input("Fibonnaci place: "))
  list = [0, 1]
  for i in range(1, x+1):
    list.append(list[i]+ list[i-1])
  return list[-3]
print(fib())
    
  