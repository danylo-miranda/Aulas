tupla = ('josean','matheus','arthur','danylo')

for i in tupla:
    print('Sejam bem vindo !',i)
    
nova_tupla = (4,) + tupla[1:]  # Cria uma nova tupla com o elemento 4 no lugar do elemento 1 da tupla original
print(nova_tupla)  # Output: (4, matheus, arthur, danylo)

#Nesse exemplo, a tupla original('josean','matheus','arthur','danylo')  foi "alterada" para (4, matheus, arthur, danylo) através da criação de uma nova tupla nova_tupla, que possui o elemento 4 no lugar do elemento 1 da tupla original.