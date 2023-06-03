def acenderlampada (): #Funções sem parâmetros não recebem nada na entrada e fornecem saída
    return print('Lampada acesa')

#acenderlampada()

##declaração da função
def produzircamiseta(tamanho,estampa):
    print(f'Camiseta com estampa ({estampa}) produzida no tamanho {tamanho}.') #F-STRING permite inserir parametros dentro das chaves
##chamada da função
#tamanho = input('insira o tamanhdo da camiseta ')
#estampa = input('insira a estampa que você deseja ')
#produzircamiseta(tamanho, estampa)

def qualcidade(cidade,pais = 'Brasil'): #atividade aula 13
    return print(f'Cidade localizada no páis Brasil')
cidade = input('Em que cidade você mora ? ')    
qualcidade(cidade)
