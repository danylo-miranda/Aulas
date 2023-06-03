from funcoes import *

carro = Carro('Modelo do veículo: Fuscão 1500','Cor do veículo: Azul',50,30,15,30)
carro.get_modelo()
carro.get_cor()
carro.get_consumo_medio()
carro.km_maximo()
carro.km_esperado()
carro.consumo_atual()
print('*' * 30) #agradecer a Lu
carro.set_modelo(input('Insira o modelo do veiculo: ')) #compliquei
carro.set_cor(input('Insira a cor do veículo: '))
carro.set_capacidade_tanque(int(input('Insira a capacidade total do tanque: ')))
carro.set_consumo_medio(int(input('Qual o consumo medio do veiculo: ')))
carro.set_litros_disponiveis(int(input('Insira a quantidade de litros disponiveis: '))) #compliquei
carro.set_kmrodado(int(input('Quantos Km tem a viagem ? '))) #compliquei
carro.km_maximo()
carro.km_esperado()
carro.consumo_atual()
print('*' * 30)



    