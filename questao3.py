chances = 5
palavra_secreta = 'batata'
while chances > 0: 
    palavra = input(f"Qual a palavra secreta? Você tem {chances} chances  ")
    chances -= 1
    if palavra == 'batata':
        print("Você acertou a palavra, toma aqui uma batata 🥔")
        break
#quando voce digita a palavra batata (palavra secreta) voce aciona o break oque encerra o loop
#quando voce nao acerta a palavra secreta o numero de chances/contador acaba oque fqaz o while sr verdadeir 
