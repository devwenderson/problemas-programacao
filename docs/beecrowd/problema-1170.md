```python
n = int(input())
for i in range(n):
    c = float(input())
    dias = 0
    while c > 1:
        dias += 1
        c = c / 2
    print(f"{dias} dias")
```