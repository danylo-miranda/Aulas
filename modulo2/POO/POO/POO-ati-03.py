from datetime import datetime #importa a biblioteca responsavel por inserir data e hora

class Perguntas():
    
    respostas = []
    
    def questoes(self):
        self.idade = input('Insira sua idade: ')                
        self.genero = input('Qual é o seu gênero? ')
        print('\n Para responder o questionário utilize : Sim (1), Não (2), Não sei responder (3)?')
        self.p1 = input('\nCompraria um carro pela internet? ')        
        self.p2 = input('\nSe o preço do carro fosse 15% abaixo do valor de mercado, você compraria? ')
        self.p3 = input('\nTem intenção de comprar um carro nos próximos 6 meses? ')
        self.p4 = input('\nGostaria do serviço de despachante na compra do seu carro? ')    
    
    
    def add_lista(self):  #método criado para fazer o questionamento das 6 perguntas e registrar data e hora                   
        self.respostas.append([self.idade])
        self.respostas.append([self.genero]) 
        self.respostas.append([self.p1])
        self.respostas.append([self.p2])
        self.respostas.append([self.p3])
        self.respostas.append([self.p4])
        hora_atual = datetime.now() #Registra o horário
        data_e_hora_atual = hora_atual.strftime('%d/%m/%Y %H:%M') #registra a data e implementa o horário da variável 'hora atual'.
        self.respostas.append(data_e_hora_atual)               
        
    def verificar_pesquisa(self): 
        while True:            
            if self.p1 not in ['1','2','3']:
                insere = input('Insira 1, 2 ou 3')
                self.respostas.append(insere)                
            else:
                print(self.respostas)
    
    def imprimir(self):
        return print(self.respostas)                         

questionario = Perguntas()
questionario.questoes()
questionario.add_lista()
questionario.imprimir()




