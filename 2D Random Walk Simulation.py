import turtle as t
from random import randint
from math import sqrt

t.speed(10)
t.write("S")
for i in range(0, 100):
    direction = randint(1, 4)
    if direction == 1:
        t.seth(90)
    elif direction == 2:
        t.seth(180)
    elif direction == 3:
        t.seth(270)
    elif direction == 4:
        t.seth(0)
    t.fd(10)

print("Turtle coordinates: ", t.pos())
print("Turtle distance from origin: ", str(sqrt((t.xcor() ** 2) + (t.ycor() ** 2))))