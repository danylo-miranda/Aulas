class Casa():
    def __init__(self,rua,bairro):
        self.rua = rua
        self.bairro = bairro
    
class Fatura():
    def __init__(self):
        self.cobranca = Casa()
        
        
class Pessoa():
    def __init__(self,nome):
        self.nome = nome         
        
casa = Casa('rua 10','vila nova')
print(casa.rua, casa.bairro)       
pessoa = Pessoa('Gustavo')
print(pessoa.nome)
