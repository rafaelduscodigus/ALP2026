maior = float('-inf')
#nehum numeso e maior que infinito o certo e -inf
soma = 0 
while soma <= 10:
    #nao existe uma variavel soma para o while rodar
    soma += 1 
    #a variavel soma serve como contador
    num = int(input("Digite um número: "))
    if num > maior:
       maior = num
print('O maior número é', maior)
