import time
import random
def exibir_mensagem():  
    print("a INFO1A é top")
    
def exibir_elogio(nome):
    print(f"{nome} é top")
    
    
def classificar_nota(nota):
     if nota > 60:
         print("aprovado")
     else:
         print("reprovado")
def contagem_regressiva(a):
     for i in range(a):
         print(i)
         time.sleep(1)

def roleta():
    numero = random.randint(1, 36)

    if numero % 2 == 0:
        cor = "Preto"
    else:
        cor = "Vermelho"

    return numero, cor

numero, cor = roleta()

      
exibir_mensagem()
exibir_elogio("Rafael")

nota = int(input("quanto voce tirou na prova? "))
classificar_nota(nota)
contagem_regressiva(5)
print(numero, cor)
