print('Insira dois números de 0 a 10')
n1 = float(input('1º número: '))
n2 = float(input('2º número: '))
if (n1 and n2 > 10) or (n1 and n2 < 0):
    print('Você não inseriu um número de 0 a 10')
else:
    s = n1+n2
    m = n1*n2
    p = n1**n2
    print(f'{n1} + {n2} = {s}\n{n1} x {n2} = {m}\n{n1} ^ {n2} = {p}')