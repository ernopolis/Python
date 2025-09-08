print('Insira dois números')
n1 = int(input('1º número: '))
n2 = int(input('2º número: '))
print('Agora decida se quer multiplicar ou dividir um pelo outro')
print('Digite x para multiplicar')
print('Digite / para dividir')
op = input('Digite >')
if op == 'x' :
    resp = n1*n2
    print(f'O resultado: {n1} x {n2} = {resp}')
elif op =='/':
    resp = n1/n2
    print(f'O resultado: {n1} / {n2} = {resp}')
else:
    print('Opção inválida!')
