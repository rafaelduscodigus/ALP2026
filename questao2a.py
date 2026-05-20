N = int(input("Quantos números quer digitar?"))
contador = 0
#contador devia ser 0 pois nao foi feita nenhuma tentativa
impares = 0

while contador < N:
    #nao e <= e sim < pois se for <= vai ter uma numero a mais pra ser digitado
    num = int(input("Digite um número: "))
    #o while nunca vai ser true pois falta a variavel contador += 1 
    contador += 1 
    if num % 2 != 0:
        impares += 1
print(f"voce digitou {impares} numeros impares")
#erro de logica pois a variavel N é quantos numero a pessoa vai digitar 
