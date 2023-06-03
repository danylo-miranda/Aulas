num = 0.9764
print(f'1: Numero = {num}')
print('2: Numero = %.4f' % num) # %d (int) - %f (float) - %s (str)
print('3: Numero = ', num)
print('4: Numero = ' + str(num))

#esse código mostra 4 tipos de saidas diferentes
# %d (int)
# %f (float)
# %s (str)

mensagem = ''
while(mensagem != 'sair'):
    mensagem = input('Digite uma mensagem ')
    print(mensagem)
    
# estrutura de repetição While    


idade = 23

while(idade>15 and idade<30): #utilização da condição "and" aplica-se conceitos de TABELA VERDADE só será ativado se as 2 condições forem verdadeiras
    print('Você precisa ser maior de 30 ou menor que 15 para sair do loop')
    idade = int(input('digite sua idade '))

print('Obrigado!')

dia = 'terça'

while(dia == 'terça' or dia == 'quarta'): #utilização da condição "or" se uma das 2 condições forem cumpridas será ativado
    print('Você precisa escolher um dia diferente de terça ou quarta para sair do loop')
    dia = input('que dia é hoje? ')

print('Obrigadoooo!!!')