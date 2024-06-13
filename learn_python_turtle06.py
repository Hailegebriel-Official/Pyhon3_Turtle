import turtle as turtle
import time
import random


turtle.speed(10)
turtle.bgcolor("black")
turns = 100
distance = 10

for x in range(turns):
    right = turtle.right(random.randint(0,360))
    left = turtle.left(random.randint(0,360))
    turtle.color(random.choice(['blue','red','violet','yellow','orange']))
    random.choice([right,left])
    turtle.fd(distance)