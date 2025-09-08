print('Coloque as três notas e te direi quantas delas estão acima da média 60')
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
n3 = float(input('Nota 3: '))
acima = 0
if n1 >= 60:
    acima = acima+ 1
if n2 >= 60:
    acima = acima+ 1
if n3 >= 60:
    acima = acima+ 1
print(f'Há {acima} notas acima da média de 60.')