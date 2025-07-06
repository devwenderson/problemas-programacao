pulo_sapo, num_canos = map(int, input().split())
canos = list(map(int, input().split()))

consegue_pular = False

for i in range(num_canos):
    if i == num_canos - 1:
        break
    
    cano_atual = canos[i]
    cano_proximo = canos[i + 1]
    diferenca = cano_proximo - cano_atual

    if diferenca <= pulo_sapo and pulo_sapo + diferenca >= 0:
        consegue_pular = True
    else:
        consegue_pular = False
        break

if consegue_pular == True:
    print("YOU WIN")
else:
    print("GAME OVER")