soma = 0
while True:  # loop infinito
    print("1. Açaí 300ml - R$ 12")
    print("2. Mousse - R$ 6,50")
    print("3. Salada de frutas - R$ 10")
    print("4. Fechar a conta")
     
    opçao = int(input("qual opçao do cardapio voce escolhe?"))
    if opçao == 1:
        conta = 0
        soma += 12
        print(f"sua conta agora é de {soma} reais!")
    elif opçao == 2:
        conta = 0
        soma += 6.50
        print(f"sua conta agora é de {soma} reais!")
    elif opçao == 3:
        conta = 0
        soma += 10
        print(f"sua conta agora é de {soma} reais!")
    elif opçao == 4:
        print(f"o valor total da sua conta é {soma}!")
        break
    
    
   
    
    if opçao == 0: 
        break

