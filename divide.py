num = int(input("Enter a number: "))
div2 = 0
div3 = 0
if(num % 2 == 0):
  print("It is divisible by 2")
  div2 = 1
if(sum(int(digit) for digit in str(num))) %3 == 0:
  print("It is divisible by 3")
  div3 = 1
if((num * 4)/16 == int):
  print("It is divisible by 4")
if((num * 2) %10 == 0):
  print("It is divisible by 5")
if(div2 + div3 == 2):
  print("It is divisible by 6")
if(num %7 == 0):
  print("It is divisible by 7")
if(num )