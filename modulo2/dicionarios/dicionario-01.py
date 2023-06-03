#dicionários são declarados das seguintes formas:

#forma-01
portuing = dict()
portuing ['one'] = 'um'
portuing ['two'] = 'dois'
print(portuing)

#forma-02
inglesportu = {'one':'um','two':'dois','three':'três'}

print(inglesportu)

if 'one' in inglesportu:
    print('Chave valida 01')

if 'um' in inglesportu:
    print('Chave valida 02')    

#acessando valores das chaves
print(inglesportu['two'])    
print(inglesportu.get('two'))
print(inglesportu.keys())

#acessar valores por elementos
print(inglesportu.values())

#retorna os itens de um dicionários em formato de tuplas
print(inglesportu.items())
