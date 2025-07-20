n = int(input())
def eh_primo(num):
    divisores = 2 # Num primo é divisível por 1

    if num == 2:
        return 2
    
    for i in range(2,num): 
        if num % i == 0: # Se achar outro além de 1 e eles mesmo
            divisores += 1
        if divisores > 2:
            break

    return divisores

while True:
    n += 1
    if eh_primo(n) == 2:
        break

print(n)

    

