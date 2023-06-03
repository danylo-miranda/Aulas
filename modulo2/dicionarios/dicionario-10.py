dic_telefone = {
    ('Ana','Santos'):'555-555',
    ('Maria','Nascimento'):'999-999',
    ('Paula','Melo'):'777-777'
}

for nome, sobrenome in dic_telefone:
    print(nome,sobrenome)
    
print(dic_telefone[('Maria','Nascimento')])
