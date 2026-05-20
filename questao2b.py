soma = 0
# e preciso adicionar um contador
contador = 0
while contador < 10: 
#nao e <= e sim < pois se for <= vai ter uma numero a mais pra ser digitado
#o while vai ser true quando a soma ser 10 e nao quando o usuario digitar 10 numeros
    num = int(input("Digite um número para somar: "))
    soma += num
    contador += 1 
#falta um print para imprimir a soma dos 10 numeros 
print("a soma dos numeros é", soma)

