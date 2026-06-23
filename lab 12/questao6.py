import time
import random
n = random.randint(2,10)
time.sleep(n)
print("AGORA!")
tempo0 = time.time()
input()
tempo1 = time.time()
t_gasto = round(tempo1 - tempo0, 2)
print(f"seu tempo de reaçao foi de: {t_gasto}")