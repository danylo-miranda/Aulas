def listar_resultados(entrevista, teorico, pratica, soft, candidatos):
    candidatos_aprovados = []
    for lista_candidato in candidatos:
        if lista_candidato[1] >= entrevista and lista_candidato[2] >= teorico and lista_candidato[3] >= pratica and lista_candidato[4] >= soft:
            candidatos_aprovados.append(lista_candidato)
    return candidatos_aprovados

candidatos = [['joao', 4, 4, 8, 8], ['ana', 2, 2, 8, 8], ['silvia', 8, 8, 4, 4], ['jade', 2, 2, 4, 4], ['jackeline', 6, 6, 9, 9]]

entrevista = 4
teorico = 4
pratica = 8
soft = 8

aprovados = listar_resultados(entrevista, teorico, pratica, soft, candidatos)
print(aprovados)


# a função .join junta itens da lista e são separados pelo caractere escolhido sem a necessidade de aspas e vírgulas.
#separador = '_'
#juntar = separador.join(lista_candidato) 
#print(lista_candidato)