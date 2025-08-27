vb = float(input("Qual o valor do bem a ser adquirido? "))
e = float(input("Qual o valor da entrada que deseja pagar? "))
p = float(input("Quantas parcelas desejas dividir? "))
vf = vb-e
vp = vf/p
print(f"O valor de cada parcela será: R$ {vp:.2f}")