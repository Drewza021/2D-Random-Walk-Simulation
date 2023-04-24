from random import randint
from math import sqrt

for repeat in range(0, 100):
    position = 0
    
    for i in range(0, 100):
        direction = randint(1, 2)

        if direction == 1:
            position += 1
        elif direction == 2:
            position -= 1

    print("Position:", position)