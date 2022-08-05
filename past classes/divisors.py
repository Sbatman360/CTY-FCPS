x = [2,3,5,7,9,11,15,17,23]
for i in range(2,10):
  if x[i-2]/i == 1:
    pass
  elif x[i-2]/i > 1:
    print("divisor processed")
  else:
    print("breaking")
    break