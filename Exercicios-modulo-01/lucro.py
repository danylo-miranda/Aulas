num1 = float(input("Insira o custo do produto:"))
porcentagem1 = 45
porcentagem2 = 30
resultado1 = num1 * (porcentagem1/100)
resultado2 = num1 * (porcentagem2/100)

if num1 < 20:
    print("É possível obter 45% de lucro vendendo esse produto por:", resultado1 + num1)
else:
    print("É possível obter 30% de lucro vendendo esse produto por:", resultado2 + num1)    