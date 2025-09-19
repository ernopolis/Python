a = int(input("Insira o tamanho do lado a: "))
b = int(input("Insira o tamanho do lado b: "))
c = int(input("Insira o tamanho do lado c: "))
if a + b > c and a + c > b and b + c > a:
    print("A medidados lados inseridos formarão um triângulo!")
else:
    print("As medidas inseridas não formarão um triângulo")
