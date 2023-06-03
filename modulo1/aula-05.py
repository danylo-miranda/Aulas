def calculo1(num1,num2,num3,num4):
    return (num1*num3 - num2*num4)

def calculo2(num1,num2,num3,num4):
    return (num1+num2+num3+num4)/4


num1 = float(input("Insira o primeiro número: "))
num2 = float(input("Insira o segundo número: "))
num3 = float(input("Insira o terceiro número: "))
num4 = float(input("Insira o quarto número: "))

print(calculo1(num1,num2,num3,num4))
print(calculo2(num1,num2,num3,num4))

