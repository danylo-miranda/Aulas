class Cliente():     #agreagação 2 classes que uma vai adicionar atributos na outra
    def __init__(self,nome,sobrenome,cpf):
       self.nome = nome
       self.sobrenome = sobrenome
       self.cpf = cpf
    
    

class Conta():
    def __init__(self,numero,cliente,saldo,limite):
        self.numero = numero
        self.titular = cliente
        self.saldo = saldo
        self.limite = limite
        

c = Cliente('Rafa','Pilan','4314314318')
minha_conta = Conta('123-4', c ,'R$120,00','R$500,00')

print(minha_conta.limite)