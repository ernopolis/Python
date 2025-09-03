val = float(input("Qual foi o valor de sua compra?: "))
dval = val - (val * 0.1)
if val >= 200:
    print(f"Você terá 10 por cento de desconto! Pague {dval}")
else:
    print(f"Pague {val}")
