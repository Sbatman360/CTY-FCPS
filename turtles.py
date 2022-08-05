import random
from turtle import *
#counter = 0
#while True:
  #forward(2 + 0.09*counter)
  #left(20)
  #counter +=1
  #if(counter == 500):
    #break
def spiral():
  speed(0)
  counter = 0
  while True:
    circle(15 + counter*0.5, 20)
    counter+=1
    if counter == 500:
      break
def flower():
  colormode(255)
  for i in range(50):
    
    color((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    speed(10)
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)
    penup()
    forward(5)
    right(90)
    forward(5)
    right(45 + i/4)
    pendown()

flower()

import sys
from turtle import *
forward(20)
left(90)
forward(20)
right(90)
forward(10)
right(90)
forward(20)
left(90)
forward(20)
left(90)
forward(50)
left(45)
forward(35)
left(90)
forward(35)
left(135)
forward(50)
back(50)
right(90)
forward(50)
left(90)
forward(30)
penup()
left(90)
forward(40)
right(90)
pendown()
forward(15)
right(90)
forward(15)
right(90)
forward(15)
right(90)
forward(15)
hideturtle()