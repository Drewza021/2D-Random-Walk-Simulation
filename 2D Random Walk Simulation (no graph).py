from random import randint
from math import sqrt

for repeat in range (0, 100):
    x = 0
    y = 0

    for i in range(0, 100):
        direction = randint(1, 4)
        
        if direction == 1:
            y += 1
        elif direction == 2:
            x += 1
        elif direction == 3:
            y -= 1
        elif direction == 4:
            x -= 1


    print("Final coordinates: (", x, ",", y, ")")
    print("Distance from origin: ", str(sqrt(((x ** 2) + y ** 2))))
