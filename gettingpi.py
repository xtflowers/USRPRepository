import random

hits = 0
N = 100

for i in range(N):
    x = random.random()
    y = random.random()
    if (x*x + y*y <= 1):
        hits = hits + 1

pi = 4 * (hits / N)
print (pi)
    
        
