qpc = float(input("Quantas peças você comprou para este mês?:"))
qpv = float(input("Quantas peças foram vendidas este mês?:"))
nf = float(input("Quantos funcionários você tem?:"))
gm = qpc * 5  # gastos com mercadoria
v = qpv * 7  # total de vendas no mês
gf = nf * 2000  # gastos com funcionários
L = v - gf - gm - 1400  # Lucro
if qpc < qpv:
    print("Não é possivel vender mais mercadoria do que comprou")
else:
    print(f"Este mês você obteve um lucro de {L} reais.")
