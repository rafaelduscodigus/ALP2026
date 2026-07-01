import time 
entrada = int(input("quanto tempo de pausa? "))
tempo0 = time.time()
time.sleep(entrada * 2)
tempo1 = time.time()
print("voce esperou", int(tempo1 - tempo0), "segundos")