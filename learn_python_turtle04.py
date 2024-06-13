import turtle 
import time

turtle.color("green")
def destacircle(radius):
    for angle in range(0,360,10):
        turtle.seth(angle)
        turtle.circle(radius)


if __name__ == "__main__":
    destacircle(100)
    time.sleep(10)
    turtle.bye()