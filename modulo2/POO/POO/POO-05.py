class Historico():
    def __init__(self):
        self.data_abertura = '30/05/2023'
        self.transacoes = []

class Conta():
    def __init__(self):
        self.cliente = ''
        self.hitorico = Historico() #composição 

minha_conta = Conta()
minha_conta.cliente = 'Danylo'
minha_conta.hitorico.transacoes = [1,2,3]


print(minha_conta.hitorico.data_abertura)