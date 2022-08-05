import random
points = 0 
score1 = random.randint(1,6)
score2 = random.randint(1,6)
score3 = random.randint(1,6)
if(score1 == score2 and score2 == score3):
  points += score1*100
elif(score1 == score2):
  points += score1*20
elif(score2 == score3):
  points += score2*20
elif(score3 == score1):
  points += score3*20
else:
  if score1 > score2 and score1 > score3:
    points += score1
  elif score2 > score1 and score2 > score3:
    points += score2
  else:
    points += score3
print(score1, score2, score3, points)



string1 = 'I love Mickey Mouse.'
string2 = 'Open your book to page three.'
string3 = 'My favorite sport is football.'
string4 = 'I live on Floral Avenue.'

#question 3
#print(string4[-7:] + string3[2:12] + string2[:4])

#question 2
#print(string4[:2] + string2[2:3] + string3[4:5] + string3[-6:-5]+string1[1:2]+string2[10:14]+ string1[-3:
#binary1 = input("binary: ")
#binary = binary1[::-1]
#decimal = 0
#for i in range(0, len(binary)):
 # decimal += int(binary[i]) * (2 ** i)
#print(decimal)
n = int(input('how many natural numbers do you want? '))

sum = 0 
for i in range(1, n+1):
  if(i%2 ==1):
    pass
  else:
    sum += i

print('sum is', sum)