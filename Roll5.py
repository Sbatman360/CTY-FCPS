import random
dice = []
kind = [0,0,0,0,0]
points = 0
pairs = 0
triple = 0
for i in range(5):
  dice.append(random.randint(1,6))
for m in range(0, len(dice)):
  for j in range(m+1, len(dice)):
    if dice[j] == dice[m]:
      kind[m] +=1
for c in range(0, len(kind)):
  if(kind[c] == 5):
    points += 100
  if(kind[c] == 4):
    points += 40
  if(kind[c] == 3):
    points += 10
    triple +=1
  if(triple >=1 and pairs >=1):
    points +=75
  if(kind[c] == 2):
    pairs +=1

print(points)