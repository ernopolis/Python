print("Insira três números")
n1 = float(input("1º número: "))
n2 = float(input("2º número: "))
n3 = float(input("3º número: "))
pares = 0
if n1 % 2 == 0:
    pares = pares + 1
if n2 % 2 == 0:
    pares = pares + 1
if n3 % 2 == 0:
    pares = pares + 1
if pares == 1:
    p = str("par")
else:
    p = str("pares")
print(f"Há {pares} {p} entre os números inseridos.")
