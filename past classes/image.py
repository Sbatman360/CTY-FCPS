def countprint():
  s = input("Enter a string: ")
  vowelstr = "aeiouAEIOU"
  digitstr = "0123456789"
  vowels = 0
  spaces = 0
  digits = 0
  others = 0
  for c in range(0, len(s)):
    if(s[c] in vowelstr):
      vowels +=1
    elif(s[c] in digitstr):
      digits+=1
    elif(s[c] == ' '):
      spaces +=1
    else:
      others+=1
  print('Vowels:', vowels, 'Spaces:', spaces, 'Others:', others)
value = int(input("enter a value to HOTPO: "))
initialvalue = value
steps = 0
while value != 1:
  if value % 2 == 0:
    value /= 2
    steps +=1
  else:
    value = value*3 + 1
    steps +=1