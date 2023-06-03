class Conta(): #ENCAPSULAMENTO
    def __init__(self,saldo):
        self.saldo = saldo
        
    def get_saldo(self):
        return self.saldo
    
    def set_saldo(self,saldo):
        self.saldo = saldo
        
conta1 = Conta(200)
conta2 = Conta(250)
conta3 = Conta(300)     

print(conta1.get_saldo())
print(conta2.get_saldo())


conta3.set_saldo(conta1.get_saldo() + conta2.get_saldo())

print(conta3.get_saldo())