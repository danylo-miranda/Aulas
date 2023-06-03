nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insinra a segunda nota: "))
nota3 = float(input("Insira a terceira nota: "))

aritimetica = (nota1 + nota2 + nota3) / 3 
ponderada = (nota1*3+nota2*3+nota3*2) / 8 
mensagem = f"\na media aritimética é {aritimetica:.2f} e a média ponderada é {ponderada:.2f}"

print(mensagem)