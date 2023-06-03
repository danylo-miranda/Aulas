class Pessoa():
    def __init__(self, nome, cpf):
        self._nome = nome
        self._cpf = cpf
        
    def get_nome(self):
        return self._nome 
        
    def get_cpf(self):
        return self._cpf
        
    def set_nome(self, novo_nome):
        self._nome = novo_nome
        
    def set_cpf(self, novo_cpf):
        self._cpf = novo_cpf
        
pessoas = Pessoa('joao','12312312348')
print(pessoas.get_nome())
print(pessoas.get_cpf())
pessoas.set_nome('maria')
pessoas.set_cpf('32132132138')
print(pessoas.get_nome())
print(pessoas.get_cpf())    