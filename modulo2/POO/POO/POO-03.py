class Carro():
    cor = 'amarela'
       
    def __init__(self,rodas,tanque): #inicia o metodo pré-modulado
        self.rodas = rodas
        self.litrostanque = tanque
    
    def get_cor(self): #retorna valores
        return self.cor   
    
    def set_cor(self,novacor): #modifica valores
        self.cor = novacor

carrim = Carro(4,50)
carrim.get_cor()
print(carrim.get_cor())
carrim.set_cor('Azul')
print(carrim.get_cor())