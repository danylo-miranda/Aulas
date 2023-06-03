tupla01 = (0,1,2,3,4,5,6,7,8,9) 
tupla02 = (0,1,2,3,4,5,6,7,8,9)
tupla03 = ()

# Realizando a multiplicação dos elementos de mesmo índice
for i in range(len(tupla01)):
    resultado = tupla01[i] * tupla02[i]
    tupla03 += (resultado,)
    
print(tupla03)

#Nesse exemplo, as duas tuplas tupla1 e tupla2 contêm os elementos de mesmo índice que serão multiplicados. O algoritmo itera sobre as tuplas usando um loop for e multiplica os elementos de mesmo índice usando a expressão tupla1[i] * tupla2[i]. O resultado de cada multiplicação é adicionado à tupla de resultados tupla_resultado usando a operação += junto com uma tupla contendo o resultado.
#No final, o algoritmo exibe o conteúdo da tupla tupla_resultado, que contém o resultado das multiplicações. A saída será uma tupla com os resultados correspondentes aos elementos de mesmo índice das duas tuplas originais.