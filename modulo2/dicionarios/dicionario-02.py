def buscar(gloss):
    if gloss in glossario:
        print(glossario[gloss])

glossario = {'Github':'Repositório de códigos','Git':'Versionamento de código','Laço':'Estruturas de repetição','Python':'Linguagem de programação','Syntaxe':'Gramática da linguagem'}

entrada = str(input('Insira a sua dúvida: ').title())
buscar(entrada)
