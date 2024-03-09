class BibliotecaVirtual:
    def __init__(self):
        self.libros = ["Fisica", "Calculo", "Desarrollo de Software", "Estadistica", "Bases de Datos"]
        
    def disponibilidad(self, libros):
        return libros in self.libros