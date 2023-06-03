def beberoudirigir (idade):
    if idade >= 18:
        return print('Você já pode dirigir')
    else:
        return print('Você ainda não pode dirigir')

#idade = int(input('Insira a sua idade: ')) 
#beberoudirigir(idade)

def previsao_rodagem (gasolina,km_litro):
    km_rodados = gasolina * km_litro
    return km_rodados

previsao = previsao_rodagem(7,35)
print('De acordo com os parametros apresentados é possível rodar', previsao,'km sem precisar abastecer')
