print("cardapio")
print("1. Açaí 300ml - R$ 12")
print("2. Mousse - R$ 6,50")
print("3. Salada de frutas - R$ 10")
print("4. Fechar a conta")
soma = 0 

while True:
    opcao = int(input("qual opcao voce deseja? "))
    if opcao == 1:
        soma += 12
    elif opcao == 2:
        soma += 6.50
    elif opcao == 3:
        soma += 10
    elif opcao == 4:
        break
    else:
        print("voce digitou um numero invalido.")
        continue
print(f"o total da sua conta foi {soma}$ ")