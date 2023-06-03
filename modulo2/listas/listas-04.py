nomes = ['rafael', 'marina', 'will', 'miguel']
print(nomes[0:4]) #fatiamento de string 

nome = ['rafael', 'marina', 'will', 'miguel']
lista_copia = nome[:] #o comando '[:]' clona a lista e atribui a variavel declarada

nome [1] = 'teste' #substituir um iten da lista

print(lista_copia)
print(nome)