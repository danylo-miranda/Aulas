pacientes = int(input("Insira o número de pacientes:"))
for i in range(pacientes):
    print(f"\nDados do paciente {i+1}:")
    nome = (input(f"Qual o nome do pciente {i+1}: "))
    altura = float(input("Qual a altura do paciente? "))
    peso = float(input("Informe o peso do paciente:"))
    imc = peso / (altura*altura)
    print(f"Dados do paciente {i+1}:")
    print(f"Nome: {nome}")
    print(f"Altura: {altura:.2f} mt's")
    print(f"Peso: {peso:.2f} kg")
    print(f"IMC: {imc:.2f}")

dicionario = print("\nIndice de medida corporal: \n Abaixo de 18.5    | abaixo do peso \n entre 18.6 e 24.9 | peso ideal \n entre 25.0 e 29.9 | levemente acima do peso \n entre 30.0 e 34.9 | obesidade grau 1 \n entre 35.0 e 35.9 | obesidade grau 2 Severa \n acima de 40       | obesidade 3 morbida ")

print(dicionario)

#Temas: Estruturas de repetição, Entrada de dados, Operadores matemáticos, Saída de dados, Python

#Classificação: Intermediário

#O que é para fazer:

#Escreva uma programa em Python que peça a quantidade de pacientes e calcule o IMC a partir do nome, peso e altura para cada um deles.

#Como Fazer:

#Crie uma variável que vai armazenar o número de pacientes;
#Crie um for para percorrer a quantidade de pacientes;
#Crie variáveis para armazenar nome, altura e peso;
#Crie uma variável para calcular o IMC e faça o cálculo necessário;
#Imprima os dados na tela.