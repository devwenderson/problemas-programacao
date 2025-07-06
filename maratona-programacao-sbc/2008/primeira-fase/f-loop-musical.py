# APARENTEMENTE, A LÓGICA ESTÁ INCORRETA

while True:
    n_amostras = int(input())
    if n_amostras == 0:
        break
    magnitudes = list(map(int, input().split()))
    picos = 0
    
    for i in range(n_amostras):
        atual = magnitudes[i]
        anterior = magnitudes[(i + n_amostras - 1) % n_amostras]
        proximo = magnitudes[(i + 1) % n_amostras]

        if anterior < atual and proximo < anterior:
            picos += 1
        elif anterior > atual and proximo > atual:
            picos += 1

    print(picos)
