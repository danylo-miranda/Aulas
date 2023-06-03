class Carro():   
    
    def __init__(self, modelo, cor, capacidade_tanque, qnt_combustivel_tanque, consumo_medio, kmrodado): #construtor
        self.modelo = modelo
        self.cor = cor
        self.capacidade_tanque = capacidade_tanque
        self.qnt_combustivel = qnt_combustivel_tanque
        self.consumo_medio = consumo_medio
        self.kmrodado = kmrodado     
            
    def km_maximo(self): #Quantos KM o veiculo pode rodar de acordo com o consumo médio em relação a capacidade total do tanque
        kmtotal = self.consumo_medio * self.capacidade_tanque #calcula qnt maxima de km de acordo com a capacidade total do tanque
        return print(f'Capacidade do tanque de {self.capacidade_tanque}Lts e é suficiente para rodar {kmtotal}km')
    
    def km_esperado(self):#calculo com a expectativa de rodagem de acordo com o combustivel disponivel em relação ao consumo medio
        kmesperado = self.consumo_medio * self.qnt_combustivel 
        return print(f'A expectativa de rodagem com {self.qnt_combustivel}Lts é de:{kmesperado}Km')
    
    def consumo_atual(self):#calculo que subtrai 1 litro de combustivel de acordo com o consumo medio
        combustivel_necessario = self.kmrodado / self.consumo_medio #obter o valor que será subtraido na qnt de combustivel
        if combustivel_necessario <= self.qnt_combustivel: #qnt de combustivel deve ser menor do que a quantidade necessaria para rodar
            self.qnt_combustivel -= combustivel_necessario #subtrai a qnt de combustivel necessario pela qnt de combustivel disponivel e atribui o resultado na variavel combustivel_necessario
            print(f'Quantidade de combustivel disponivel após rodar {self.kmrodado}KM: {self.qnt_combustivel:.2f} Litros')
            kmrestante = self.qnt_combustivel * self.consumo_medio #calcula a qnt de km que ainda pode rodar com o combustivel que sobrou
            print(f'Você ainda pode andar {kmrestante:.0f}km')#imprime a qnt de km que poderá rodar com o combustivel restante
        else:
            print('Combustivel insuficiente para essa kilometragem') #condição inserida para caso a qnt de km rodado seja maior que o combustivel disp.
    
    def get_modelo(self): #exibe o modelo do veiculo
        return print(self.modelo)             
        
    def get_cor(self): #exibe a cor do veiculo
        return print(self.cor)
    
    def get_capacidade_tanque(self): #exibe a capacidade do tanque de combustivel
        return print(self.capacidade_tanque)    
    
    def get_consumo_medio(self): #exibe o consumo de combustivel
        return print(f'Consumo medio: {self.consumo_medio} KM por litro')
    
    def set_modelo(self,novomodelo):
        self.modelo = novomodelo        
    
    def set_cor(self, novacor):
        self.cor = novacor                
    
    def set_capacidade_tanque(self,novacapacidade):
        self.capacidade_tanque = novacapacidade        
    
    def set_consumo_medio(self,novoconsumo):
        self.consumo_medio = novoconsumo
                
    def set_litros_disponiveis(self, litros):
        self.qnt_combustivel = litros            
            
    def set_kmrodado(self,novokm):
        self.kmrodado = novokm