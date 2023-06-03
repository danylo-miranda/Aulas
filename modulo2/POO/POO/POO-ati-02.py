class Pessoa():
    idade = ''
    cidade = ''
    estado = ''
    salario = ''
    escolaridade = ''
    
    def imprimir(self,idade, cidade, estado, salario, escolaridade):
        print(f'idade:{idade} anos, Cidade:{cidade}, Estado:{estado}, Salário atual:{salario}, Escolaridade:{escolaridade}')

pessoas = Pessoa()
pessoas.idade = input('Insira a idade: ')
pessoas.cidade = 'Franca'
pessoas.estado = 'São Paulo'
pessoas.salario = 'R$1600,00'
pessoas.escolaridade = 'Superior Completo'
pessoas.imprimir(pessoas.idade, pessoas.cidade, pessoas.estado, pessoas.salario, pessoas.escolaridade)