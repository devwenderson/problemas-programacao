# F - Loop musical

``` python
while True:
    n = int(input())
    if n == 0:
        break
    sequencias = list(map(int, input().split()))
    picos = 0
    for i in range(n):
        atual = sequencias[i]
        
        if i == 0:
            anterior = sequencias[-1]
            proximo = sequencias[i+1]
        elif i == len(sequencias)-1:
            anterior = sequencias[i-1]
            proximo = sequencias[0]
        else:
            anterior = sequencias[i-1]
            proximo = sequencias[i+1]

        if anterior > atual and proximo > atual:
            picos += 1
        elif anterior < atual and proximo < atual:
            picos += 1

    print(picos)

```