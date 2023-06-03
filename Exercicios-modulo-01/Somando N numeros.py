quantidade = int(input("Insira a quantidade de numeros que deseja somar: "))
soma = 0
for i in range(quantidade):
    numero = int(input(f"Insira um numero{i+1}:"))
    soma += numero
print("O valor das somas é:",soma)