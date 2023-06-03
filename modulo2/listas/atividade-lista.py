def insere (fila, elemento):
    return fila.append(elemento)

def remove (fila):
    return fila.pop(-1)

def verifica (fila):
    if len(fila) > 0:
        return print(len(fila))
    else:
        print('lista vazia')

fila = []
        
for i in range(10):
    insere(fila, i)
    
print(fila)

verifica(fila)

remove(fila)

print(fila)

fila = []

verifica(fila)
      




