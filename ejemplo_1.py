# Clase Persona

class Persona:

    # método constructor
    def __init__(self, nombre, apellidos, edad):
        self.Nombre = nombre
        self.Apellidos = apellidos
        self.Edad = edad

    # método para mostrar los datos de una persona
    def MostrarPersona(self):
        print("Nombre: " + self.Nombre)
        print("Apellidos: " + self.Apellidos)
        print("Edad: " + str(self.Edad))

# metodo principal
def main():
    p1 = Persona("Mariana", "Delgado", 14)
    p1.MostrarPersona()
    p2 = Persona("Gabriela", "Arevalo", 15)
    p2.MostrarPersona()

if __name__ == "__main__":
        main()