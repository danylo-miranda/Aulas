# A herança e o polimorfismo são conceitos poderosos que permitem que as classes compartilhem código e sejam tratadas de maneira mais genérica, aumentando a flexibilidade e a reutilização de código na programação orientada a objetos.

##### POLIMORFISMO #####

class Funcionario():
    def comissao(self, valor):
        print(valor * 0.5)
    
class Gerente(Funcionario):
    def comissao(self, valor):
        print(valor * 1.5)

rafael = Funcionario()
danylo = Gerente()

rafael.comissao(100)
danylo.comissao(100)
