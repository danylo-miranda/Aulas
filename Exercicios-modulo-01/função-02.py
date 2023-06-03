texto = input("Insira uma letra: ")
def vogal(letra):
    vogais = ['a','e','i','o','u',]
    if letra in vogais:
        return True
    else: 
        return False    
    
print(vogal(texto))


