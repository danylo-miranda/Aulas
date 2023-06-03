num1 = float(input("insira o primeiro numero: "))
num2 = float(input("insira o segundo numero: "))
num3 = float(input("insira o terceiro numero: "))

def maior(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
         return num3
print(maior(num1,num2,num3))

#Temas: Funções, Operadores lógicos, Estruturas condicionais, Python

#Classificação: Intermediário

#O que é para fazer:

#Defina uma função que usa três números como argumentos e retorna o maior deles.

#Como Fazer:

#Crie uma função para realizar o cálculo necessário;
#Dentro da função, realize condições para verificação;
#Chame a função e imprima o resultado.