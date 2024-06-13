import turtle as turtle 
import time

colors = ['green','yellow','blue','red','violet','orange']
turtle.speed(10)
turtle.bgcolor('black')

for x in range(100):
    turtle.circle(x)
    turtle.color(colors[x%6])
    turtle.left(60)