def soma(valor1,valor2):
    return valor1 + valor2

def calculadobrodasoma(valor1,valor2):
    resultado = soma(valor1,valor2)
    dobro = resultado * 2
    return dobro

#print(calculadobrodasoma(1,3))

#criar uma nova função que será utilizada dentro do retorno da função calculadobrodasoma 
#e essa função deve imprimir o resultado da seguinte forma:
#'A soma do valor1 + valor2 é igual ao resultado e seu dobro é igual ao dobro'

def print1(valor1,valor2):
    print(f'A soma de', valor1 + valor2, 'é igual ao resultado e seu dobro é igual a',calculadobrodasoma(2,4))
print1(2,4)