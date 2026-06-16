while True:
    p = input("Você quer saber como manter uma pessoa ingênua ocupada por horas?")
    if p == "sim" or p == "s" or p == "SIM" or p == "S":
        continue
    elif p == "n" or p == "N" or p == "nao" or p == "NAO":
        print("Obrigada. Tenha um bom dia!")
        break
    else:
        print(p, "não é uma resposta válida de sim/não.")
    