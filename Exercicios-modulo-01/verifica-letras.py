texto = input("Insira uma letra: ")
def vogal(letra):
    vogais = ['a','e','i','o','u',]
    if letra in vogais:
        return True
    else: 
        return False    
    
print(vogal(texto))


#Temas: Saída de dados, Python, Estruturas condicionais, Operadores lógicos

#Classificação: Intermediário

#O que é para fazer:

#Escreva uma função que receba uma string e retorne True se for uma vogal e False caso contrário

#Como Fazer:

#Crie uma função para realizar o cálculo necessário;
#Dentro da função, realize condições para verificação;
#Chame a função e imprima o resultado.