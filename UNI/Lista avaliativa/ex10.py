tc = int(input("Qual o tamanho do circuito em km? "))
dp = int(input("Qual a quantidade de km que o carro percorreu antes de acabar todo o combustíve? "))
nv = dp//tc
uv = dp%tc
print(f"O número de voltas completas foi de {nv}.\nE a distância percorrida na última volta antes de acabar o combustível foi de {uv}")
