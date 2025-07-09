s, m = map(int, input().split())
segundos = 0
minutos = 0
horas = 0
dias = 0
while m > 0.5:
    segundos += s
    m /= 2

if segundos >= 60:
    minutos = segundos // 60
    segundos = segundos % 60
    if minutos >= 60:
        horas = minutos // 60
        minutos = minutos % 60
        if horas >= 24:
            dias = horas // 24
            horas = horas % 24 

print(f"{dias} dias {horas:0>2d}:{minutos:0>2d}:{segundos:0>2d}")