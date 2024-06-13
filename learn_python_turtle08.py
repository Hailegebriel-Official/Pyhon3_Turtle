import turtle 
import time

turtle.speed(0)
turtle.bgcolor('black')
colors = ['green','pink','orange','blue']

for x in range (100):
    turtle.circle(x)
    turtle.left(12)
    turtle.color(colors[x%4])
time.sleep(10)
