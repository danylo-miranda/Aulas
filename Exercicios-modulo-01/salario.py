num1 = float(input("Insira o valor do seu salário:"))
minimo = float(1320)
quantidade = num1/minimo

if quantidade > 1:
    print("O seu salário é igual á:", quantidade, "salários mínimos")

elif quantidade < 1:
    print("Você está recebendo valores abaixo de 1 salário minimo")
