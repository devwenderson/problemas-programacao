``` python
n = int(input())
 
for i in range(n):
    dinheiro, qtd_marcas = map(int, input().split())
    precos = list(map(float, input().split()))
    maior_troco = 0
    for preco in precos:
        if preco <= dinheiro:
            qtd = dinheiro // preco
            pagamento = qtd * preco
            troco = dinheiro - pagamento
            if troco > maior_troco:
                maior_troco = troco
    print(f"{maior_troco:0.2f}")
```

Link do problema: https://www.beecrowd.com.br/repository/UOJ_1755.html