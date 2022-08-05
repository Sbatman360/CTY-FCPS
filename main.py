def b10to2(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal*2 + int(digit)


def check_palindrome(word):
  for i in range(0,len(word)):
    if (word[i] == word[-(i+1)]):
      pass
    else:
      return False
  return True
def factors(number):
  list = []
  for i in range(1, number + 1):
    if((number / i)%1 == 0):
      list.append(i)
  return list

def GCF():
  number1 = int(input("First number:"))
  number2 = int(input("Second number:"))
  f1 = factors(number1)
  f2 = factors(number2)
  if(f1 < f2):
    f1, f2 = f2, f1
  for i in range(1, len(f1)):
    for j in range(1, len(f2)):
      if(f1[-i] == f2[-j]):
        print("GCF is:", f1[-i])
        quit()
  print("GCF is: 1")
 
def calculator():
  while True:
    x = int(input("Enter an integer: "))
    y = str(input("Enter an operation: "))
    z = int(input("Enter a second integer: "))

    if(y == "+"):
      print("Answer:", x+z)
    elif(y == "x" or y == "*"):
      print("Answer:", x*z)
    elif(y == "-"):
      print("Answer:", x-z)
    elif(y == "/"):
      print("Answer:", x/z)
def find_months():
  months = ['January', 'February','March', 'April', 'May', 'June',        'July', 'August', 'September', 'October', 'November', 'December']
  number = int(input("Month Number: "))
  print("Month:", months[number-1])


# from turtle import *

# speed(0)
# forward(50)
# right(90)
# forward(50)
# right(90)
# forward(50)
# right(90)
# forward(50)
# right(60)
# forward(30)
# right(30)
# forward(50)
# right(150)
# forward(30)
# left(60)
# forward(50)
# left(120)
# forward(30)
# left(60)
# forward(50)
# left(90)
# forward(50)
# left(90)
# forward(50)
# right(60)
# forward(30)
# right(180)
# forward(30)
# right(30)
# forward(50)
# hideturtle()

# import random
# dice = []
# kind = [1,1,1,1,1]
# points = 0
# pairs = 0
# triple = 0
# for i in range(5):
#   dice.append(random.randint(1,6))
# for m in range(0, len(dice)):
#   for j in range(m+1, len(dice)):
#     if dice[j] == dice[m]:
#       kind[m] +=1
#       kind[j] =1
# if 5 in kind:
#   points += 100
# elif 4 in kind:
#   points += 40
# elif 3 in kind:
#   if 2 in kind:
#     points +=75
#   else:
#     points +=10

# def ex_args(arg1,arg2,arg3):
#   print('arg1:', arg1)
#   print("arg2:", arg2)
#   print("arg3:", arg3)

# kwargs = {'arg2':1, "arg3":"four", "arg1":6}
# ex_args(**kwargs)

def hexadecimal(input, base):
  letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', "K", "L", 'M', 'N', "O", 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', "Z"]
  base = int(base)
  x = int(input)
  hexa = ''
  while x > 0:
    carry = str(x%base)
    x = int(x / base)
    if int(carry) >= 10:
      carry = letters[int(carry)-10]
    hexa += carry
  return (hexa[::-1])

    
# import math

# prompt = input("YES to start in decimal and NO to start in other base:")
# if prompt == 'yes' or prompt == 'YES':
#   dec = int(input("Enter a decimal number to convert:"))
#   base = input("New base: ")
#   letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', "K", "L", 'M', 'N', "O", 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', "Z"]
#   base = int(base)
#   x = int(dec)
#   hexa = ''
#   while x > 0:
#     carry = str(x%base)
#     x = int(x / base)
#     if int(carry) >= 10:
#       carry = letters[int(carry)-10]
#     hexa += carry
#   print(hexa[::-1])


# else:
#   letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', "K", "L", 'M', 'N', "O", 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', "Z"]
#   original = input("Enter starting base: ")
#   number = input("number to convert:")
#   finalbase = int(input("Base to convert to: "))
#   dec = 0
#   number = list(number)
#   print(number)
#   for i in range(0, len(number)):
#     if ord(number[-i] > 64):
#       for m in range(0, len(letters)):
#         if letters[m] == number[-i]:
#           number[-i] == str(m + 10)
#     number[-i] = str(int(number[-i]) * finalbase**i)
#   print(number)
#   for j in range(0, len(number)):
#     dec += int(number[j])
#   print(dec)
#   print(hexadecimal(dec, finalbase))

def fibonacci(number):
  if(number == 1 or number == 0):
    return 1
  else:
    return fibonacci(number -1) + fibonacci(number-2)

def steps(x, y):
  if x == 0 and y == 0:
    return 1
  if x < 0 or y < 0:
    return 0
  else:
      return steps(x-1, y) + steps(x, y-1)



def multiply(x, y):
  if x == 1:
    return y
  else:
    return multiply(x-1, y) + y

from turtle import *
# for m in range(0, 4):
#     for j in range(0, 4):
#         for i in range(0, 12):
#             forward(10)
#             left(60)
#             forward(10)
#             right(120)
#         left(60)
#     left(60)
speed(0)
# for m in range(0, 3):
#     for j in range(0, 6):
#         for i in range(0, 3):
#             left(60)
#             forward(10)
#             right(120)
#             forward(10)
#         left(60)
#         forward(10)
#         left(60)
#         forward(10)   
#     left(60)
#     forward(10)
#     right(120)
#     forward(10)  

# def
# def curve(x):
#   if x < 5:
#     forward(x)
#     return
#   curve(x/3)
#   left(60)
#   curve(x/3)  
#   right(120)
#   curve(x/3)
#   left(60)
#   curve(x/3)

# def snowflake(x):
#   curve(x)
#   right(120)
#   curve(x)
#   right(120)
#   curve(x)
#   right(120)
# penup() 
# goto(-200,100)
# pendown()
# snowflake(100)
# update()
    

# hideturtle()
from turtle import *

speed(0)
    

def drawtree(size):
  if size <= 15:
    forward(15)
    backward(15)
  else:
    forward(size)
    left(30)
    drawtree(size*0.8)

    right(60)
    drawtree(size*0.8)

    left(30)
    backward(size)
goto(0, -300)
left(90)
drawtree(200)




