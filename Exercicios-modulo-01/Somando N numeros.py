quantidade = int(input("Insira a quantidade de numeros que deseja somar: "))
soma = 0
for i in range(quantidade):
    numero = int(input(f"Insira um numero{i+1}:"))
    soma += numero
print("O valor das somas é:",soma)

#Temas: Python, Saída de dados, Entrada de dados, Operadores matemáticos, Estruturas condicionais, Estruturas de repetição

#Classificação: Iniciante

#O que é para fazer:

#Escreva um programa em Python que some diversos números fornecidos pelo usuário. A quantidade de números que serão somados, também deve ser fornecida pelo usuário.

#Como Fazer:

#Crie uma variável para receber a quantidade de números que serão somados a ser fornecida pelo usuário;
#Crie um laço para percorrer a quantidade de vezes que o usuário informarna variável anterior;
#Crie as variáveis de número e soma;
#Realize o cálculo necessário;
#Imprima a informação para o usuário.