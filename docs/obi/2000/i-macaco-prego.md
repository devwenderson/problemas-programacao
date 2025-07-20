```python
n_teste = 1
while True:
    n_regioes = int(input())
    if n_regioes == 0:
        break
    
    x_base = -10000
    y_base = 10000
    u_base = 10000
    v_base = -10000

    for i in range(n_regioes):
        x,y,u,v = map(int, input().split())

        if x > x_base:
            x_base = x
        if y < y_base:
            y_base = y
        if u < u_base:
            u_base = u
        if v > v_base:
            v_base = v
    
    if x_base > u_base or v_base > y_base:
        print(f"Teste {n_teste}")
        print("nenhum\n")
    else:
        print(f"Teste {n_teste}")
        print(f"{x_base} {y_base} {u_base} {v_base}\n")
    
    n_teste += 1
```