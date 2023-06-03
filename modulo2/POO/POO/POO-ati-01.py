class cachorro():
    lista = []
    
        
    def nome_cachorro(self):
        nome = input('Qual o nome do cachorro ? ')
        self.lista.append(nome)
    def idade_cachorro(self):
        idade = input('Qual a idade do cachorro ? ')
        self.lista.append(idade)
        
    def latir(self):
        print('O cachorro latiu ')
        
    def comer(self):  
        print('O cachorro comeu ')
        
    def exibir(self):
        print(self.lista)
    
    
dogao = cachorro()
dogao.nome_cachorro()            
dogao.idade_cachorro()
dogao.latir()
dogao.comer()
dogao.exibir()
        

