# entrada de dados
d1 = float(input("1ª Dimensão em metros:"))
d2 = float(input("2ª Dimensão em metros:"))
# processamento
a = d1 * d2
pot = a * 18
# saída de dados
print(
    f"{a} metros quadrados de área e {pot}W de potência "
    + "necessários para iluminar seu quarto."
)
