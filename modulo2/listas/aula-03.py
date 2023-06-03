lista_zeros = [0] * 10

for valor in lista_zeros:
    print(valor)

print('=================')

for i in range (len(lista_zeros)):
    print(lista_zeros[i])
    
lista = []

for i in range (2,12,2): # de 0 a 12 soma de 2 em 2 e a cada 2 casas ele adiciona 1 iten na lista
    lista.append(i)
print(lista)

#1. append(): Adiciona um elemento ao final da lista;
#2. insert(): Adiciona um elemento em uma posição específica da lista;
#3. remove(): Remove a primeira ocorrência de um elemento na lista;
#4. pop(): Remove e retorna o último elemento da lista (ou um elemento em uma posição específica);
#5. index(): Retorna a posição da primeira ocorrência de um elemento na lista;
#6. sort(): Ordena a lista em ordem crescente.

lista1 = [1]

for i in range(1,11):
    lista1.append(i)
lista.pop(1) #remove o iten da lista de acordo com a posição indicada
print(lista1)

letras = ['d','c','b','e','a']

letras.sort()
print(letras)