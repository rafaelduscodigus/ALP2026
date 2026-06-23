import random
import time
n = random.randint(0, 10)
print(n)
n_voltas = 0 
for i in range(n):
    n_voltas += 1
    print(f"volta {n_voltas}: Mais uma volta!")
    time.sleep(1)
