def calculadora(a, b, op):
    if op == "+":
        return f"a soma dos dois numeros é: {a + b}"
    elif op == "-":
        return f"a subtraçao dos dois numeros é: {a - b}"
    elif op == "*":
        return f"a multiplicaçao dos dois numeros é: {a * b}"
    elif op == "/":
        return f"a divisao dos dois numeros é: {a / b}"
a = int(input("escola o primeiro numero: "))
b = int(input("escola o segundo numero: "))
op = input("escolha o operador: ")
print(calculadora(a, b, op))
