class listadecompras():
    lista = []

    def inserir_itens(self):
        msg = input('Insira um iten na lista ')
        self.lista.append(msg)
    def consultar(self):
        print(self.lista)
        
while True:
    print('*'*30)
    print('1 - Inserir novo iten ')
    print('2 - consultar itens ')
    print('3 - sair')
    print('*'*30,'\n')
    
    option = input('Insira uma opção: ')
    
    if option == '1':
        listajaneiro = listadecompras()
        listajaneiro.inserir_itens()
        
    elif option == '2':
        listajaneiro.consultar()
        
    else:
        option == '3'
        break