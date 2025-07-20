``` python
while True:
    h1, m1, h2, m2 = map(int, input().split())
    if h1 == 0 and m1 == 0 and h2 == 0 and m2 == 0:
        break

    minutos1 = (h1 * 60) + m1
    minutos2 = (h2 * 60) + m2

    if minutos1 < minutos2:
        minutos_passados = minutos2 - minutos1
    else:
        minutos_passados = (minutos2 - minutos1) + 1440
    print(minutos_passados)
```