# E - Mergulho

``` python
n, r = map(int, input().split())
retornaram = list(map(int, input().split()))

if n == r:
    print("*")
else:
    existe = False
    for i in range(1, n+1):
        for j in retornaram:
            if j == i:
                existe = True
                break
            else:
                existe = False
        if existe == False:
            print(f"{i}", end = ' ')
```