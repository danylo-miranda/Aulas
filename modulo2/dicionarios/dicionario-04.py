glossario = {'Github':'Repositório de códigos','Git':'Versionamento de código','Laço':'Estruturas de repetição','Python':'Linguagem de programação','Syntaxe':'Gramática da linguagem'}

glossario.update({'Git':'Git bash'})

glossario.popitem()

glossario.pop('Github')

del glossario ['Laço']
print(glossario) 