print('Insira três notas de 0 a 10')
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
n3 = float(input('Nota 3: '))
m = (n1+n2+n3)/3
if m >= 6:
    print('Aluno aprovado!')
else: 
    print('Aluno terá de fazer recuperação')
    r = float(input('Qual foi a nota de recuperação do aluno?: '))
    mr = (m+r)/2
    if mr >= 6:
        print('Aluno foi aprovado em recuperação')
    else:
        print('Aluno falhou na recuperação.')