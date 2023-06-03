pessoas = ['Maria', 'João', 'Pedro', 'Julia', 'Lucas']

respostas = {'Maria': 'Python', 'João': 'C++'}

for i in pessoas:
    if i in respostas:
        print(f"Obrigado por responder, {i}!")
    else:
        print(f"{i}, não esqueça de responder a enquete sobre sua linguagem favorita!")
