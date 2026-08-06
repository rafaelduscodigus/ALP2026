def converter(c):
    f = (c * 1.8) + 32
    return (f"{c} graus celsius em fahrenheit é {f}")
x = float(input("digite a temperatura em celsius: "))
print(converter(x))