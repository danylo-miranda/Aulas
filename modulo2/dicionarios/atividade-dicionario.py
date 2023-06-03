cidade01 = {
    ('Fortaleza','Ceará'):'Tem praia',
    ('São Paulo','São Paulo'):'Não tem praia',
    ('Belo Horizonte','Minas Gerais'):'Não tem praia'
}

for cidade, estado in cidade01:
    print(cidade,estado)
    
print(cidade01[('Fortaleza','Ceará')])