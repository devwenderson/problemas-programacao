# Problema 1755 do beecrowd
n = int(input())

# Casos de testes
for i in range(n):
    quantia_joao, qtd_marcas = map(int, input().split())
    precos = list(map(float, input().split()))
    trocos = []
    for p in precos:
        trocos.append(quantia_joao % p)
    maior_troco = max(trocos)
    print(f"{maior_troco:.2f}")


