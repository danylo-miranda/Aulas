salario = float(input("Insira o valor do seu salário: "))

if salario <= 600:
    desconto = salario * 0
elif salario <= 1200:
    desconto = salario * (20/100)
elif salario <= 2000:
    desconto = salario * (25/100)
else:
    desconto = salario * (30/100)        
    
mensagem = f"Serão descontados o valor de R$ {desconto:.2f}"
print(mensagem)
    
    
#Temas: Python, Entrada de dados, Operadores matemáticos, Estruturas condicionais, Saída de dados

#Classificação: Intermediário

#O que é para fazer:

#Escreva um programa em Python que exiba o desconto do INSS segundo seu salário. Por exemplo, se o usuário possuir salário inferior ou igual a R$: 600,00 ele será isento, em caso de maior que R$: 600,00 e menor ou igual a R$:1.200,00, o desconto é de 20%; em caso de Maior que R$: 1.200,00 e menor ou igual a R$: 2.000,00, o desconto é de 25%; e em caso de maior que R$: 2.000,00, o desconto é de 30%.

#Como Fazer:

#Crie uma variável para receber o salário do usuário;
#Crie uma condição para fazer as verificações necessárias;
#Dentro das verificações, crie a variável que vai armazenar o cálculo do desconto;
#Imprima o valor do desconto para o usuário.