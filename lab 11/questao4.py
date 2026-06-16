import time
import random

p1 = 0
p2 = 0 
c = 0

while p1 < 50 or p2 < 50:
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    c += 1    
    print(f"========== RODADA {c} ==========") 
    j1 = int(input(f"jogador 1 ({p1} pontos) qual seu palpite?"))
    j2 = int(input(f"jogador 2 ({p2} pontos) qual seu palpite?"))
    print("🎲  Rolando os dados...")
    time.sleep(2)
    print("dado1:",dado1,)
    print("dado2:",dado2,)
    if abs((dado1 + dado2) - j1) < abs((dado1 + dado2) - j2): 
        print("resultado: VITORIA! do jogador 1, ele ganhou 5 pontos")
        p1 += 5
        continue
    elif  abs((dado1 + dado2) - j1) == abs((dado1 + dado2) - j2):
         print("Resultado: ⚖️ EMPATE! Cada um ganha 2 pontos!")
         p1 += 2
         p2 += 2
         continue
    else:
        print("resultado: VITORIA! do jogador 2, ele ganhou 5 pontos")
        p2 += 5
        
    
    