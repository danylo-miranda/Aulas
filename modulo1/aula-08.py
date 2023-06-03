num1 = int(input("Insira um numero: "))

for i in range(num1):  #a letra "i" é referente a inteiro 
    if i % 3 == 0:
        print(i)    

#Um laço for é utilizado assim como o while até que a condição torne-se falsa.
# Ela é utilizada percorrendo o intervalo de controle/contagem definido em range
#(início, fim, incremento).


num1 = int(input("insira um numero inteiro: "))

while (num1 >= 0):
           
    print(num1)
    num1 = num1 - 1