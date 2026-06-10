cont = 5
while cont > 0: 
    num = int(input("Digite um número inteiro: "))
    cont -= 1
    if num % 2 == 0: 
        continue
    print(f'{num} é um número ímpar')
#quando vc digita um numero impar ele ignora o if e armazena o valor e imprime ignorando o continue
#quando um numero par e digitado ele faz o if virar true e o comando continue ativa fazendo o loop voltar e n rodar o resto 