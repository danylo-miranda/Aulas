nome = input("insira o nome do aluno: ")
nota1 = float(input("Insira o valor da primeira nota: "))
nota2 = float(input("Insira o valor da segunda nota: "))
nota3 = float(input("Insira o valor da terceira nota: "))
notame = float(input("Insira o valor da nota ME: "))

MA = (nota1 + nota2 * 2 + nota3 * 3 + notame)/7

print('Aluno ' + str(nome) + ', obteve nota média final de: %.2f' % MA )

if (MA > 9):
    print('Você foi aprovado com média A')
elif (MA > 7.5):
    print('Você foi aprovado com média B')
elif (MA > 6):
    print('Você foi aprovado com média C')
elif (MA > 4):
    print('Você foi reprovado com média D')
else:
    print('Você foi reprovado com média E')
    
# exercício final da aula 10 ^^^^

#aula 11

sentenca = "essa é uma string"
for i in range(len(sentenca)): #A função "len" retorna a quantidade de caracteres contidos em uma string, ou seja, seu comprimento.
    print(sentenca[i])
    
    
#replace 
#print(sentenca.replace(" ","*")) #essa opção troca caracteres


#lower #utilizado para deixar as letras minusculas
#print(sentenca.lower())

#upper #utilziado para deixar todas as letras maiusculas
#print(sentenca.upper())

#find
#indice = sentenca.find('uma')
#print(indice)    