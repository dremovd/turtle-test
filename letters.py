from turtle import pendown, right, forward, left, penup, circle, speed, color, done, setposition
import random

left(90)
def буква_а():
    pendown()
    right(20)
    forward(100)
    right(140)
    forward(100)
    right(180)
    forward(42)
    left(70)
    forward(40)
    right(180)
    forward(40)
    right(70)
    forward(42)
    penup()
    left(160)

def буква_ю():
    pendown()
    forward(100)
    right(180)
    forward(50)
    left(90)
    forward(50)
    left(180)
    left(90)
    circle(50)
    penup()
    forward(50)
    left(90)
    forward(100)
    left(90)

penup()
setposition(-300, 0)
color('green')
speed(30)
letters = [буква_а, буква_ю]
for _ in range(5):
    random.choice(letters)()
done()