import turtle
import time

def square(length):
    for i in range(4):
        turtle.fd(length)
        turtle.left(90)

    
if __name__ == "__main__":
    square(150)
    time.sleep(10)  
    turtle.bye()