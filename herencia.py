# Clase Persona

class Persona:
    
    # método constructor
    def __init__(self):
        self.__Nombre = "Mariana"
        self.__Apellidos = "Delgado"
        self.__Edad = 14

    def getNombre(self):
        return self.__Nombre
    
    def setNombre(self, nombre):
        self.__Nombre = nombre

    def getApellidos(self):
        return self.__Apellidos
    
    def setApellidos(self, apellidos):
        self.__Apellidos = apellidos

    def getEdad(self):
        return self.__Edad
    
    def setEdad(self, edad):
        self.__Edad = edad

    # método para mostrar los datos de una persona
    def MostrarPersona(self):
        print("Nombre: " + self.__Nombre)
        print("Apellidos: " + self.__Apellidos)
        print("Edad: " + str(self.__Edad))

class Alumno(Persona):
    def __init__(self):
        self.__Curso = ""
        self.__Asignaturas = ""
    
    def getCurso(self):
        return self.__Curso
    
    def setCurso(self, curso):
        self.__Curso = curso

    def getAsignaturas(self):
        return self.__Asignaturas
    
    def setAsignaturas(self, asignaturas):
        self.__Asignaturas = asignaturas

    def mostrarAlumno(self):
        print("Alumno")
        print("\tNombre: ", self.getNombre())
        print("\tApellidos: ", self.getApellidos())
        print("\tEdad: ", self.getEdad())
        print("\tCurso: ", self.__Curso)
        print("\tMatrículas: ", self.__Asignaturas)

class Profesor(Persona):
    def __init__(self):
        self.__antiguedad = 0
        self.__tutorias = ""
        self.__telefono = 0

    def getAntiguedad(self):
        return self.__antiguedad
    
    def setAntiguedad(self, antiguedad):
        self.__antiguedad = antiguedad

    def getTutorias(self):
        return self.__tutorias
    
    def setTutorias(self, tutorias):
        self.__tutorias = tutorias
    
    def setTelefono(self, telefono):
        self.__telefono = telefono

    def getTelefono(self):
        return self.__telefono
    
    def mostrarProfesor(self):
        print("Profesor")
        print("\tNombre: ", self.getNombre())
        print("\tApellidos: ", self.getApellidos())
        print("\tEdad: ", self.getEdad())
        print("\tAntiguedad: ", self.__antiguedad)
        print("\tTutorias: ", self.__tutorias)


        

# metodo principal
def main():
    alumno = Alumno()
    alumno.setNombre("Mariana")
    alumno.setApellidos("Delgado Solano")
    alumno.setEdad(14)
    alumno.setCurso("Bachillerato")
    alumno.setAsignaturas(["Matematicas", "Tecnologia", "Ingles"])
    alumno.mostrarAlumno()

    # profesor

    profesor = Profesor()
    profesor.setNombre("Nestor")
    profesor.setApellidos("Paez Sarmiento")
    profesor.setEdad(30)
    profesor.setAntiguedad(15)
    profesor.setTutorias(["Sistemas 1"])
    profesor.setTelefono("222 222 2222")
    profesor.mostrarProfesor()

if __name__ == "__main__":
    main()
