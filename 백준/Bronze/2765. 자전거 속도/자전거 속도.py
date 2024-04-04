import math
import os

f = os.read(0, os.fstat(0).st_size)
tokens = iter(f.split())
iterations = 1
while True:
    perimeter, revolutions, time = float(next(tokens)),float(next(tokens)),float(next(tokens))
    if revolutions == 0:
        break
    distance = perimeter*math.pi*revolutions/5280/12
    speed = distance/time*3600
    print(f"Trip #{iterations}: {round(distance, 2):.2f} {round(speed, 2):.2f}")
    iterations += 1