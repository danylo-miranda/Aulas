num1 = float(input("Insira o custo do produto:"))
porcentagem1 = 45
porcentagem2 = 30
resultado1 = num1 * (porcentagem1/100)
resultado2 = num1 * (porcentagem2/100)

if num1 < 20:
    print("É possível obter 45% de lucro vendendo esse produto por:", resultado1 + num1)
else:
    print("É possível obter 30% de lucro vendendo esse produto por:", resultado2 + num1)    
    
#Temas: Entrada de dados, Operadores matemáticos, Operadores lógicos, Estruturas condicionais, Python, Saída de dados

#Classificação: Iniciante

#O que é para fazer:

#Um lojista comorou diversos produtos para sua loja e deseja revendê-lo com margem de lucro diferente dependendo do valor; por exemplo, ele deseja obter lucro de 45% caso o produto custe menos que R$ 20,00. Porém, caso o produto custe mais que isso, o lucro deve ser de 30%. Escreva um programa em Python que ajude esse lojista.

#Como Fazer:

#Crie uma variável para receber o valor do produto;
#Crie uma condição para verificar a condição solicitada;
#Dentro da condição, realize o cálculo necessário.
#Imprima as informações para o usuário.