def insere_nafila (fila, elemento):
    return fila.append(elemento) # adiciona um elemento no fim da lista

def romeve_dafila (fila):
    return fila.pop(0) # .pop remove o primeiro iten da lista

fila = []

for i in range(10):
    insere_nafila(fila, i)
    
print(fila)
romeve_dafila(fila)
print(fila)