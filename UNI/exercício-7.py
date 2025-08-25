s = int(input("Quantos segundos são?: "))
sf = s%60
mp = s//60
mf = mp%60
hf = mp//60
print(f'{hf} horas, {mf} minutos e {sf} segundos')