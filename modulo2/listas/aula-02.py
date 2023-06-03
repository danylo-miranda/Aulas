# intalação de pacotes e criação de ambiente virtual
#"installPip"
# Set-ExecutionPolicy -Scope CurrentUser Unrestricted
# python -m ensurepip --upgrade 
# pip install virtualenv
# UPDATE pip install virtualenv 

# LISTAS: As listas são uma das estruturas de dados mais utilizadas em Python e são amplamente utilizadas em diferentes tipos de aplicativos. Facilidade de uso, flexibilidade e a possibilidade de operações avançadas são algumas das principais características de sua popularidade.


lista1 = [10, 20, 30]
print(lista1[0])

lista2 = ['sapo', 'jacare', 'cobra']
print(lista2[0])

lista3 = [10, 20, ['jacare', 'cobra']]
print(lista3[2][1])

lista1[0]= 10*10
print(lista1)

# Atividade:

lista_nome = ['danylo', 'daniel', 'gideoni', 'rafael']

for i in lista_nome:
    print('Seja bem vindo', i)

concatenar = lista1 + lista2
print(concatenar)

zeros = [0] * 4
print(zeros)

if 'cobra' in lista2:
    print('A cobra é um animal exotico')

