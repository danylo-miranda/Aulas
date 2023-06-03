lista_nome = ['danylo', 'daniel', 'gideoni', 'rafael']
lista_facilitador = ['Rafa', 'Will', 'José']
lista_final = lista_nome + lista_facilitador

for i in lista_final:
    print('Seja bem vindo', i)
    
if 'Rafa' or 'Will' or 'José' in lista_final:
    print('Os nomes dos facilitadores estão na lista')
else:
    print('Os nomes dos facilitadores não estão na lista')
       
