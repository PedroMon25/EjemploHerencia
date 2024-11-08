# main.py
from estudiantes import Estudiantes
from profesores import Profesores
from administrativos import Administrativos
from empleado_limpieza import EmpleadoLimpieza

def main():
    # Crear objetos
    estudiante = Estudiantes()
    estudiante.set_nombre("Sergio")
    print(estudiante.get_nombre())
    estudiante.set_carrera("Ing. arquitecto")
    estudiante.set_semestre("2")
    estudiante.set_apellido("Castro")
    estudiante.set_edad(20)
    estudiante.set_matricula("07770")

    profesor = Profesores()
    profesor.set_nombre("Fernando")
    profesor.set_max("Maestria")
    profesor.set_categoria("Maestro")
    profesor.set_apellido("Monroy")
    profesor.set_edad(40)
    profesor.set_departamento("Quimica")

    administrativo = Administrativos()
    administrativo.set_area("Administracion")
    administrativo.set_nombre("Carlos")
    administrativo.set_apellido("Valle")
    administrativo.set_edad(35)
    administrativo.set_cargo("Secretario")

    empresa = EmpleadoLimpieza()
    empresa.set_turno("matutino")
    empresa.set_nombre("Pedro")
    empresa.set_apellido("Montalbo")
    empresa.set_edad(45)
    empresa.set_numero_empleado("0525")
    empresa.set_nombre_empresa("Limpieza S.A.")
    empresa.set_direccion("Calle Ficticia Av.Hola")

    # Mostrar información
    print("Estudiante:")
    print(estudiante.mostrar_informacion())

    print("\nProfesor:")
    print(profesor.mostrar_informacion())

    print("\nAdministrativo:")
    print(administrativo.mostrar_informacion())

    print("\nEmpleado de Limpieza:")
    print(empresa.mostrar_informacion())

if __name__ == "__main__":
    main()