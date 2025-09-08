dividendo = int(input('Insira o dividendo: '))
divisor = int(input('Insira o divisor para a divisão: '))

quo = dividendo/divisor
res = dividendo % divisor
if divisor == 0:
    print('Esta divisão não é possivel!')
else:
    print(f'O quociente é {quo} e o resto é {res}')