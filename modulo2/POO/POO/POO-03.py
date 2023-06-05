class Carro():
    cor = 'amarela'
       
    def __init__(self,rodas,tanque): #metodo construtor inicia os atributos junto com classe
        self.rodas = rodas 
        self.litrostanque = tanque
    
    def get_cor(self): #'get_' retorna valores
        return self.cor   
    
    def set_cor(self,novacor): # 'set_' modifica valores
        self.cor = novacor

carrim = Carro(4,50)
carrim.get_cor()
print(carrim.get_cor())
carrim.set_cor('Azul')
print(carrim.get_cor())