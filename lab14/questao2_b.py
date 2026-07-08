def ola(nome, genero):
    if genero == "neutro":
        return f"ola {nome}, boas vindas" 
    elif genero == "feminino":
        return f"ola {nome}, bem vinda"
    elif genero == "masculino":
        return f"ola {nome}, bem vindo"
print(ola("leo", "neutro"))
print(ola("mila", "feminino"))
print(ola("alan", "masculino"))