```python
n = int(input())

while n != 1:
    if n % 2 == 0:
        n //= 2
        print(n)
    else:
        n = (n * 3) + 1
        print(n)
```

Link do problema: https://cses.fi/problemset/task/1068