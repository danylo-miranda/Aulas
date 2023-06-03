#lista de dicionários

carro01 = {'cor':'preto', 'motor':'2.0', 'ano':'2012'}
carro02 = {'cor':'vermelho', 'motor':'1.6', 'ano':'2016'}
carro03 = {'cor':'prata', 'motor':'1.8', 'ano':'1988'}
carro04 = {'cor':'branco', 'motor':'2.0', 'ano':'2013'}

lista_carros = [carro01,carro02,carro03,carro04]

#percorre todos os itens da lista e imprime
for carro in lista_carros:
    print(carro)

print(lista_carros[0]['motor'])

dic_carros = {
    'gol':carro01,
    'onyx':carro02,
    'chevete':carro03,
    'celta':carro04    
}

for item in dic_carros.items():
    print(item)
#A função .items() é uma função nativa de Python que pode ser utilizada em dicionários. Ela retorna uma lista de tuplas, onde cada tupla contém a chave e o valor correspondente no dicionário.