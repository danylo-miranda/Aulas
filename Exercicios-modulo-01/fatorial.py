def fatorial(numero):
    if numero == 1:
        return 1
    return numero * fatorial(numero-1)
print(fatorial(3))

#Temas: Saída de dados, Python, Funções, Entrada de dados

#Classificação: Avançado

#O que é para fazer:

#Escreva um programa que possa calcular o fatorial de um determinado número. Os resultados devem ser impressos em uma sequência separada por vírgulas em uma única linha. Suponha que a seguinte entrada é fornecida para o programa: 8 Em seguida, a saída deve ser: 40320

#Como Fazer:

#Crie uma função para realizar o cálculo necessário;
#Fora da função, crie uma variável para receber o número do usuário;
#Chame a função e imprima o resultado.