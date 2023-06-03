class Gato():
    nome = ''
    data_nascimento = ''
    raca = ''
    
    def miar(self, nome):
        print('O gato',nome,'mioou !')
    
    def comer(self, nome):
        print('O gato',nome,'comeu ')

gato = Gato()

gato.nome = 'katchau'
gato.raca = 'Frajola'
gato.data_nascimento = '25/05/2023'
gato.miar(gato.nome)
gato.comer(gato.nome)
print(gato.nome)
print(gato.raca)
print(gato.data_nascimento)