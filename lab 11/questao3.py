import time 
import random
while True:
    p = input("voce deseja fazer uma pergunta? ")
    if p == "nao":
        break
    elif p == "sim":
        pergunta = input("qual a sua duvida?  ")
        prob = random.randint(1, 10)      
        if prob <= 5: 
            resposta = 'SIM'
        else: 
            resposta = 'NÃO'
    print("deixe-me pensar......")
    time.sleep(2)
    print("estou quaseee!")
    time.sleep(2)
    print("eu tenho uma resposta!")
    time.sleep(2)
    print(resposta)
