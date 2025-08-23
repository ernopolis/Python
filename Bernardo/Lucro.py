qpv = float(input("Quantas peças foram vendidas este mês?:"))
nf = float(input("Quantos funcionários você tem?:"))
gm = qpv * 5
v = qpv * 7
gf = nf * 2000
L = v - gf - gm - 1400
print(f"Este mês você obteve um lucro de {L} reais.")
