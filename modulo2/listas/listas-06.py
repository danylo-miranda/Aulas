frutas = ['maça', 'laranja', 'limao', 'banana', 'kiwi', 'pessego']

nova_lista = []

#for i in frutas:     
#    if 'a' not in i:
#        nova_lista.append(i)
# para cada elemento da lista > ele verifica > se não tiver a letra 'a' ele vai adicionar o elemento a nova_lista
maiuscula = [i.upper() for i in frutas] #utilizar letras maiusculas
nova_lista = [i.title() for i in frutas if 'a' not in i] #list comprehension      
print(maiuscula)
print(nova_lista)