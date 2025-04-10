#Desarrola un programa que tilice la POO para registrar un libro (ISBN, titulo
class Libro:
    def __init__(self):
        self.__isbn:int
        self.__titulo:str=""
        self.__autor:str=""

    def getIsbn (self)->int:
        return self.isbn
    def getTitulo (self)->str:
        return self.titulo
    def getAutor (self)->str:
        return self.autor

class Biblioteca:
    def __init__(self):
        self.lista=[]

    def addLibro(self, isbn, titulo, autor):
        self.lista.append(Libro(isbn, titulo, autor))

    def show (self):
        for obj in self.lista:
            print(f"isbn: {obj.isbn}")
            print(f"Titulo: {obj.titulo}")
            print(f"Autor: {obj.autor}")
            print("_______________________")

if __name__ == '__main__':

    libro=Biblioteca()
    libro.addLibro(123,"hbh", "hbch")
    libro.addLibro(123,"hbh", "hbch")
    libro.addLibro(123,"hbh", "hbch")
    libro.addLibro(123,"hbh", "hbch")

    libro.show()

