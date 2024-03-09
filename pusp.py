from administrador import Administrador
from alquilerBicicleta import AlquilerBicicleta
from alquilerEquipo import AlquilerEquipo
from bibliotecaVirtual import BibliotecaVirtual
from estudiante import Estudiante

class Pusp:
    def __init__(self):
        self.administradores = []
        self.alquilerBicicletas = []
        self.alquilerEquipos = []
        self.biblioteca = BibliotecaVirtual()
        self.estudiantes = []
    
    def registroEstudiante(self, nombre, usuario, contrasena, idEstudiante):
        registroEstu = Estudiante(nombre, usuario, contrasena, idEstudiante)
        self.estudiantes.append(registroEstu)
        print("\nEl estudiante ha sido registrado.")
        
    def registroAdministrador(self, administrador):
        self.administradores.append(administrador)
        print("\nEl administrador ha sido registrado.")
    
    def ingresoEstudiante(self, usuario, contrasena):
        for estudiante in self.estudiantes:
            if estudiante.usuario == usuario and estudiante.contrasena == contrasena:
                print(f"\nBienvenido a la PUSP {estudiante.nombre}")
                return estudiante
        print("Error en el ingreso... Estudiante no encontrado.")
    
    def ingresoAdministrador(self, usuario, contrasena):
        for administrador  in self.administradores:
            if administrador.usuario == usuario and administrador.contrasena == contrasena:
                print("\nBienvenido a la PUSP")
                return True
        return("Error en el ingreso... Administrador no encontrado.", False)
    
    def alquilarBicicleta(self, idEstudiante):
        placaBicicleta = int(input("Ingrese la placa de la bicicleta: "))
        for alquilerBicicleta in self.alquilerBicicletas:
            if alquilerBicicleta.placaBicicleta == placaBicicleta and alquilerBicicleta.disponibilidad:
                print("Bicicleta reservada.")
                alquilerBicicleta.disponibilidad = False
                return
            print("Error... Bicicleta no reservada.")
    
    def alquilarEquipo(self, idEstudiante):
        nombreEquipo = int(input("Ingrese el numero del equipo: "))
        for alquilerEquipo in self.alquilerEquipos:
            print("Equipo alquilado.")
            return
        print("Error... Equipo no disponible")
        
    def ventas(self, idEstudiante):
        producto = input("Ingrese el nombre del producto: ")
        print(f"{producto} ha sido comprado correctamente. ")
        
    def prestarLibro(self, libros):
        self.bibliotecaVirtual.append(libros)
        
    def reporte(self, administrador):
        print("Equipos alquilados: ")
        for alquilerEquipo in self.alquilerEquipos:
            print(f"{alquilerEquipo.nombreEquipo}")
        
        print("Bicicletas alquiladas: ")
        for alquilerBicicleta in self.alquilerBicicletas:
            print(f"\n{alquilerBicicleta.placaBicicleta}")
       