from administrador import Administrador
from alquilerBicicleta import AlquilerBicicleta
from alquilerEquipo import AlquilerEquipo
from bibliotecaVirtual import BibliotecaVirtual
from estudiante import Estudiante
from pusp import Pusp 

def app():
    while True:
        print("\n---MENU DE OPCIONES---\n1. Ingreso estudiante. \n2. Ingreso administrador. \n3. Salida.")
        op = int(input("Escoja una opcion: "))
        
        if op == 1:
            while True:
                print("Bienvenido al menu de Estudiante...")
                print("1. Ingresar \n2. Registrarse \n3. Volver al menu principal")
                opEst = int(input("Escoja una opcion: "))
                
                if opEst == 1:
                    usuario = input("Ingrese su usuario: ")
                    contrasena = input("Ingrese la contrasena: ")
                    estudiante = Pusp().ingresoEstudiante(usuario, contrasena)
                    if estudiante:
                        while True:
                            print("---MENU DE SERVICIOS---")
                            print("1. Realizar restamo bicicleta \n2. Realizar prestamo equipo \n3. Realizar compras \n4. Realizar prestamo bibliotecario \n5. Volver al menu de servicios")
                            opEst2 = int(input("Escoja una opcion: "))
                            if opEst2 == 1:
                                Pusp().alquilarBicicleta(estudiante.idEstudiante)
                            elif opEst2 == 2:
                                Pusp().alquilarEquipo(estudiante.idEstudiante)
                            elif opEst2 == 3:
                                Pusp().ventas(estudiante.idEstudiante)
                            elif opEst2 == 4:
                                Pusp().prestarLibro()
                            elif opEst2 == 5:
                                break
                            else:
                                print("Seleccione una opcion valida.")
                    elif opEst2 == 3:
                        break
                    else:
                        print("Seleccione una opcion valida. ")
                
                if opEst == 2:
                    nombre = input("Ingrese su nombre: ")
                    usuario = input("Ingrese el usuario deseado: ")
                    contrasena = input("Ingrese la contrasena deseada: ")
                    idEstudiante = input("Ingrese su codigo de estudiante: ")
                    Pusp().registroEstudiante(nombre, usuario, contrasena, idEstudiante)
                
                if opEst == 3:
                    while True:
                        print("\nBienvenido al menu de Administrador...")
                        print("1. Ingresar \n2. Volver al menu de Administrador")

                        opAdmi = int(input("Escoja una opcion: "))

                        if opAdmi == 1:
                            usuario = input("Ingrese su usuario: ")
                            contrasena = input("Ingrese su contrasena: ")

                            if Pusp().ingresoAdministrador(usuario, contrasena):
                                print("Acceso concedido. ")
                            
                            else:
                                print("Acceso denegado. ")

                        elif opAdmi ==2:
                            break
                        else:
                            print("Error... Escoja una opcion valida.")
                
                elif opAdmi == 3:
                    print("Usted ha salido correctamente. ")

                else:
                    print("Error... Escoja una opcion valida.")       