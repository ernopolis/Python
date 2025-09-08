a = int(input("Digite um número de 4 dígitos: "))
d1 = a // 1000
s1 = a % 1000
d2 = s1 // 100
s2 = s1 % 100
d3 = s2 // 10
s3 = s2 % 10
d4 = s3 // 1
print(f"{d1}\n{d2}\n{d3}\n{d4}")
