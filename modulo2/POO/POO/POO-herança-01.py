# A herança e o polimorfismo são conceitos poderosos que permitem que as classes compartilhem código e sejam tratadas de maneira mais genérica, aumentando a flexibilidade e a reutilização de código na programação orientada a objetos.

##### HERANÇA #####

class Funcionario():
    def __init__(self, nome, cpf, salario):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
        
class Gerente(Funcionario): # objeto gerente herda todos os atributos da classe funcionario
    def __init__(self, senha, qnt_funcionarios):
        self.senha = senha
        self.qnt_funcionarios = qnt_funcionarios
        
gerente = Gerente('1234',4) # objeto gerente herda todos os atributos da classe funcionario
gerente.salario = 400
print(gerente.salario)