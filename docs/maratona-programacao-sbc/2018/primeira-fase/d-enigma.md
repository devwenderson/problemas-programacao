# D - Enigma

```python
men_cifrada = input()
crib = input()

posicoes_possiveis = 0
num_deslocamentos = len(men_cifrada) - len(crib)
letras_analisar = len(crib)-1

for i in range(num_deslocamentos + 1):
    # Cria um intervalo da mensagem cifrada para analisar
    letras_analisar += 1
    intervalo_cifra = men_cifrada[i:letras_analisar]
    for j in range(len(crib)):
        if intervalo_cifra[j] == crib[j]:
            letras_diferentes = False
            break
        else:
            letras_diferentes = True
    if letras_diferentes:
        posicoes_possiveis += 1

print(posicoes_possiveis)

```