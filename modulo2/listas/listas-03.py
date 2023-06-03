lista = []

# Lê a lista de números
for i in range(15):
    lista.append(int(input(f'Digite o {i+1}º número: ')))
    
lista = [i for i in lista if i % 2 == 0] # Remove os elementos ímpares
lista.sort() # Ordena a lista # Utilize reverse=True para ordem decrescente
print(lista) # Após a função .sort() Exibe o menor e o maior valor

#Este algoritmo lê uma lista de 15 números digitados pelo usuário, remove os elementos ímpares, ordena a lista resultante e exibe do menor para o maior valor desta lista. Note que foi utilizada uma lista por compreensão para remover os elementos ímpares e o método sort() para ordenar a lista em ordem crescente.