# PEP - 8 Buenas practicas de escritura Pyhon 
class Libro:
    # atributo de clase: globales
    pasta_dura = "azul"

    #contructor inicializador
    #(__) -> Metodos Magicos
    def __init__(self, titulo, autor, pag):
        #atributos de instancia
        self.titulo = titulo
        self.autor = autor
        self.paginas = pag
        self.tipo = "Papel"




    def __str__(self) -> str:
        return f"{self.titulo} - {self.autor}"
    
    def leer_Libro(self, pag):
        print(f"Estamos leyendo la pagina {pag}.")

if __name__ == "__main__":
    print("*"*50)
    
    # crear objetos o instancia
    #Instanciasion de la clase libro 
    p1 = Libro("HP1", "S", 350)
    p2 = Libro("ESDLA", "Tolkien", 400 )
    print(p1)
    print(f"titulo : {p1.titulo}, el autor es: {p1.autor}, y tiene {p1.paginas} paginas")
    p1.leer_Libro(12)

    biblioteca = []
    biblioteca.append(Libro("EALC","Anonimo",50))
    print(biblioteca)

    for libro in biblioteca:
        print(libro)

    print("*"*50)           
