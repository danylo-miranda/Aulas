#sentenca = "essa é uma string"

#for i in range(len(sentenca)):
 #   print(sentenca[::-1][i]) # nessa linha foi utilizado "::-1" que serve para inverter a contagem da função LEN
#print(len(sentenca[:]))

#replace 
#print(sentenca.replace(" ","*")) #essa opção troca caracteres


#lower #utilizado para deixar as letras minusculas
#print(sentenca.lower())

#upper #utilziado para deixar todas as letras maiusculas
#print(sentenca.upper())

#find
#indice = sentenca.find('uma')
#print(indice)

str = 'X-DSPAM-Confidence:0.8475'
posicao = str.find(':') + 1 # encontra a posição do sinal de dois pontos e adiciona 1 para começar a fatiar depois dele
numero = float(str[posicao:]) # fatia a string depois do sinal de dois pontos e converte em um número float
resultado = numero * 100 # multiplica o número por 100
print(resultado)
