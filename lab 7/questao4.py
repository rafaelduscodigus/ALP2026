
import random # essa deve ser a primeira linha do código
chances = 5 
numero = random.randint(1, 10)
while chances > 0:
    n = int(input(f"qual numero voce escolhe? (voce tem {chances} tentativas)  "))
    chances -= 1
    if n == numero:
        print("voce acertou!")
        break
print("o numero certo era:", numero)



