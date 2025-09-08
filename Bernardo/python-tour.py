"""x = 0
while x < 10:
    print(x)
    x = x + 1

print("ACABOU")
# caminha em elementos de 1 ate 10
for i in range(1, 10):
    print(f"i = {i}")

r = range(1, 10)

print(type(r))

for x in xs:
    print(f"x={x}")

# Nao enche o saco pow
# x1 = int(input("x1="))
# x2 = int(input("x2="))
# x3 = int(input("x3="))

# xs = [x1, x2, x3]

n = int(input("Quantos elementos? :"))

xs = []  # lista vazia

print(f"len(xs)={len(xs)}")  # qtd de items na lista

for i in range(0, n):
    x = int(input(f"xs[{i}]: "))
    xs.append(x)  # lista xs cresce

    print(f"len(xs)={len(xs)}")  # qtd de items na lista


print("THE WHOLE THING")
print(xs)


ys = [0, 1] * n
print(f"ys={ys}")
for i in ys:
    ys[i] = int(input(f"y[{i}]: "))

zs = [3, 7]

z1 = zs[0]  # gets the 0th guy
z2 = zs[1]

print(f"z1={z1}")
"""
