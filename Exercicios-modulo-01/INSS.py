salario = float(input("Insira o valor do seu salário: "))

if salario <= 600:
    desconto = salario * 0
elif salario <= 1200:
    desconto = salario * (20/100)
elif salario <= 2000:
    desconto = salario * (25/100)
else:
    desconto = salario * (30/100)        
    
mensagem = f"Serão descontados o valor de R$ {desconto:.2f}"
print(mensagem)
    