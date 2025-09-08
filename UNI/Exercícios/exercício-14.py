print('Insira três números')
n1 = float(input('1º número: '))
n2 = float(input('2º número: '))
n3 = float(input('3º número: '))
if n1 > n2 and n3:
    maior = n1
if n2 > n1 and n3:
    maior = n2
if n3 > n1 and n2:
    maior = n3
if n1 < n2 and n3:
    menor = n1
if n2 < n1 and n3:
    menor = n2
if n3 < n1 and n2:
    menor = n3
print(f'O maior número digitado foi {maior} e o menor foi {menor}')