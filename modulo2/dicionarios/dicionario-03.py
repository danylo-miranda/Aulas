inglesportu = {'one':'um','two':'dois','three':'três'}

#atribuição
inglesportu ['one'] = 'uno'

#usando metodo update
inglesportu.update({'two':'dos'})

#remover pela chave
inglesportu.pop('one')
del inglesportu['two']

#remove pelo ultimo iten
inglesportu.popitem()

#esvaziar todo o dincionario
inglesportu.clear()

print(inglesportu)