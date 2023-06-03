mensagem = float(input("Qual é a temperatura do paciente ? "))
 
while (mensagem != 0):
    
    if mensagem >= 40:
        print("O paciente está com febre alta !")
        break            
    elif mensagem >= 38:
        print("O paciente está com febre !")        
        break
    else:
        print("O paciente não está com febre.")
        break
    
encerramento = input("Digite sair para encerrar o programa: ")

while (encerramento == "sair"):
    print("Obrigado por utilizar nosso programa.")
    break

        