soma = 0
while True:
  n = int(input("digite um numero para somar: "))
  if n < 0:
      continue
  soma += n 
  if soma > 100 or n == 0:
      break 
print("a soma dos numeros que voce digitou e: ", soma)   
