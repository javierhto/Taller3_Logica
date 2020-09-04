# Taller 2 Lógica - Grupo 3
# En este taller se debe modelar el diagnóstico médico, aplicando lógica difusa, para
# determinar el grado de Influenza que padece un paciente (leve, moderada, alta, muy alta) y
# con ello ser una ayuda al especialista para que este posteriormente pueda realizar la
# elección de un tratamiento más adecuado. Para el desarrollo de la aplicación informática
# debe utilizar el lenguaje de programación Python y la librería scikit-fuzzy para generar 3
# representaciones gráficas que expliquen el trabajo realizado con los conjuntos difusos, las
# reglas de inferencias y los cálculos para la obtención de los resultados.

# Follow this example: https://pythonhosted.org/scikit-fuzzy/auto_examples/plot_tipping_problem.html

import skfuzzy as fuzz   # Check the documentation here: https://pythonhosted.org/scikit-fuzzy/userguide/getting_started.html
import numpy as np

# Definición clase paciente
class Pacient:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

# Función que muestra todos los datos del paciente
def printPacient(pacient):
    print("### Datos del paciente ###")
    print("Nombre: " + pacient.name)
    print("Edad: " + str(pacient.age))
    print("Peso: " + str(pacient.weight))


print("                             #   #   #")
print("Bienvenido al sistema de diagnóstico de influenza de los estudiantes")
print("de Ingeniería Infomática de la Universidad Santiago de Chile\n")

print("A continuanción obtener algunos datos personales, si prefiere no")
print("contestar, rellene el campo con un '?'")

# Datos personales

# Nombre
name = input("Ingrese su nombre: ")
if name == '?':
    name = "paciente"

# Edad
if name != "paciente":
    age = int(input("Estimada/o " + name + " ingrese su edad: "))
else:
    age = int(input("Estimada/o ingrese su edad: "))

# Peso
if name != "paciente":
    weight = int(input("Estimada/o " + name + " ingrese su peso en kilogramos: "))
else:
    weight = int(input("Estimada/o ingrese su peso en kilogramos: "))

# Creación del objeto paciente
pacient = Pacient(name, age, weight)

# Muestra los datos del paciente por pantalla
printPacient(pacient)

# Recolección de los datos de síntomas del paciente

