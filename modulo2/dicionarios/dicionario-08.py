#função ZIP

lista01 = [1,2,3,4,5]
lista02 = ['a','b','c','d','e']

for item1, item2 in zip(lista01,lista02):
    print(f'item 1: {item1}, item 2: {item2} ')
    
    
#A função zip() em Python é uma função nativa da linguagem que permite combinar dois ou mais iteráveis (como listas, tuplas ou conjuntos) em um único objeto iterável, produzindo uma série de tuplas em cada iteração.

#O objetivo do zip() é unir elementos de iteráveis correspondentes, ou seja, o primeiro elemento de cada iterável é combinado, o segundo elemento de cada iterável é combinado, e assim sucessivamente, até que todos os elementos dos iteráveis sejam combinados.

