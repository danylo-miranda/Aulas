class Livro():
    def __init__(self, titulo, isbn):
        self.titulo = titulo
        self.isbn = isbn
    
    def ler(self):
        self.ler1
        print('esta lendo de forma fisica')
    
class Ebook(Livro):
    def __init__(self, link):
        self.link = link

    def ler(self):
        self.ler1
        print('esta lendo de forma digital')
    
    
ebook = Ebook('www.teste.com')

ebook.titulo = 'Teste'
print(ebook.titulo)
print(ebook.ler())
print(ebook.link)

