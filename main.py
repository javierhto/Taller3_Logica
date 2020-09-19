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
import matplotlib.pyplot as plt


######################################################
######################################################
# Definición de variables universales
# Se define el array de cada uno de los sintomas y de cada rango de las variables linguisticas
# ( Un largo de 10 con rangos entre [0,5]->bajo [0,10]->medio [5,10]->alto )
# Dolor de cabeza

x_headache = np.arange(0, 11, 1)
headache_lo = fuzz.trimf(x_headache, [0, 0, 5])
headache_md = fuzz.trimf(x_headache, [0, 5, 10])
headache_hi = fuzz.trimf(x_headache, [5, 10, 10])
# Vomito y nauseas
x_vomit = np.arange(0, 11, 1)
vomit_lo = fuzz.trimf(x_vomit, [0, 0, 5])
vomit_md = fuzz.trimf(x_vomit, [0, 5, 10])
vomit_hi = fuzz.trimf(x_vomit, [5, 10, 10])
# Dolores musculares
x_musclePain = np.arange(0, 11, 1)
musclePain_lo = fuzz.trimf(x_musclePain, [0, 0, 5])
musclePain_md = fuzz.trimf(x_musclePain, [0, 5, 10])
musclePain_hi = fuzz.trimf(x_musclePain, [5, 10, 10])
# Fatiga
x_fatigue = np.arange(0, 11, 1)
fatigue_lo = fuzz.trimf(x_fatigue, [0, 0, 5])
fatigue_md = fuzz.trimf(x_fatigue, [0, 5, 10])
fatigue_hi = fuzz.trimf(x_fatigue, [5, 10, 10])
# congestion
x_congestion = np.arange(0, 11, 1)
congestion_lo = fuzz.trimf(x_congestion, [0, 0, 5])
congestion_md = fuzz.trimf(x_congestion, [0, 5, 10])
congestion_hi = fuzz.trimf(x_congestion, [5, 10, 10])
# Escalofrios
x_shivers = np.arange(0, 11, 1)
shivers_lo = fuzz.trimf(x_shivers, [0, 0, 5])
shivers_md = fuzz.trimf(x_shivers, [0, 5, 10])
shivers_hi = fuzz.trimf(x_shivers, [5, 10, 10])
# Tos y dolor de garganta
x_cough = np.arange(0, 11, 1)
cough_lo = fuzz.trimf(x_cough, [0, 0, 5])
cough_md = fuzz.trimf(x_cough, [0, 5, 10])
cough_hi = fuzz.trimf(x_cough, [5, 10, 10])
# Fiebre
x_fever = np.arange(0, 11, 1)
fever_lo = fuzz.trimf(x_fever, [0, 0, 5])
fever_md = fuzz.trimf(x_fever, [0, 5, 10])
fever_hi = fuzz.trimf(x_fever, [5, 10, 10])
# Influenza
x_influenza = np.arange(0, 16, 1)
influenza_lo = fuzz.trimf(x_influenza, [0, 0, 5])
influenza_md = fuzz.trimf(x_influenza, [0, 5, 10])
influenza_hi = fuzz.trimf(x_influenza, [5, 10, 15])
influenza_vhi = fuzz.trimf(x_influenza, [10, 15, 15])

######################################################
######################################################

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


def validateInput(data, inferior, superior):
    flag = True
    while flag:
        while not(data.isdigit()):
            print("El número ingresado debe estar entre,",inferior,"y",superior,"\n")
            data = input("Ingrese un nuevo valor: ")
        if inferior <= int(data) <= superior:
            flag = False
            data = int(data)
        else:
            print("El número ingresado no es valido")
            data = "invalid"
    return data





"""
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
"""
######################################################
######################################################

# Graficas
# Se grafica lo que se tiene de momento (de 3 en 3 para no saturar la imagen con graficos)
fig0, (ax0, ax1, ax2) = plt.subplots(nrows=3, figsize=(8, 9))

ax0.plot(x_headache, headache_lo, 'b', linewidth=1.5, label='Leve')
ax0.plot(x_headache, headache_md, 'g', linewidth=1.5, label='Moderado')
ax0.plot(x_headache, headache_hi, 'r', linewidth=1.5, label='Alto')
ax0.set_title('Dolor de cabeza')
ax0.legend()

ax1.plot(x_vomit, vomit_lo, 'b', linewidth=1.5, label='Leve')
ax1.plot(x_vomit, vomit_md, 'g', linewidth=1.5, label='Moderado')
ax1.plot(x_vomit, vomit_hi, 'r', linewidth=1.5, label='Alto')
ax1.set_title('Nausea y vomitos')
ax1.legend()

ax2.plot(x_musclePain, musclePain_lo, 'b', linewidth=1.5, label='Leve')
ax2.plot(x_musclePain, musclePain_md, 'g', linewidth=1.5, label='Moderado')
ax2.plot(x_musclePain, musclePain_hi, 'r', linewidth=1.5, label='Alto')
ax2.set_title('Dolor muscular')
ax2.legend()

# Turn off top/right axes
for ax in (ax0, ax1, ax2):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.show()

fig1, (ax3, ax4, ax5) = plt.subplots(nrows=3, figsize=(8, 9))

ax3.plot(x_fatigue, fatigue_lo, 'b', linewidth=1.5, label='Leve')
ax3.plot(x_fatigue, fatigue_md, 'g', linewidth=1.5, label='Moderada')
ax3.plot(x_fatigue, fatigue_hi, 'r', linewidth=1.5, label='Alta')
ax3.set_title('Fatiga')
ax3.legend()

ax4.plot(x_congestion, congestion_lo, 'b', linewidth=1.5, label='Leve')
ax4.plot(x_congestion, congestion_md, 'g', linewidth=1.5, label='Moderado')
ax4.plot(x_congestion, congestion_hi, 'r', linewidth=1.5, label='Severa')
ax4.set_title('Congestion nasal')
ax4.legend()

ax5.plot(x_shivers, shivers_lo, 'b', linewidth=1.5, label='Leves')
ax5.plot(x_shivers, shivers_md, 'g', linewidth=1.5, label='Moderados')
ax5.plot(x_shivers, shivers_hi, 'r', linewidth=1.5, label='Altos')
ax5.set_title('Escalofrios')
ax5.legend()

# Turn off top/right axes
for ax in (ax3, ax4, ax5):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.show()


fig2, (ax6, ax7, ax8) = plt.subplots(nrows=3, figsize=(8, 9))

ax6.plot(x_cough, cough_lo, 'b', linewidth=1.5, label='Leve')
ax6.plot(x_cough, cough_md, 'g', linewidth=1.5, label='Moderada')
ax6.plot(x_cough, cough_hi, 'r', linewidth=1.5, label='Alta')
ax6.set_title('Tos y dolor de garganta')
ax6.legend()

ax7.plot(x_fever, fever_lo, 'b', linewidth=1.5, label='Leve')
ax7.plot(x_fever, fever_md, 'g', linewidth=1.5, label='Moderada')
ax7.plot(x_fever, fever_hi, 'r', linewidth=1.5, label='Alta')
ax7.set_title('Fiebre')
ax7.legend()

ax8.plot(x_influenza, influenza_lo, 'b', linewidth=1.5, label='Leve')
ax8.plot(x_influenza, influenza_md, 'g', linewidth=1.5, label='Moderada')
ax8.plot(x_influenza, influenza_hi, 'r', linewidth=1.5, label='Alta')
ax8.plot(x_influenza, influenza_hi, 'r', linewidth=1.5, label='Muy alta')
ax8.set_title('Nivel de influenza')
ax8.legend()


# Turn off top/right axes
for ax in (ax6, ax7, ax8):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.show()

######################################################
######################################################

#Valores de entrada#

print("\nConsidere una escala de 0 a 10, para identificar la intensidad o ocurrencia de su(s) sintoma(s)\n>> Por ejemplo si no presenta dolor de cabeza, entonces el valor es 0 <<\n")


headache = input("Ingrese el valor para 'dolor de cabeza': ")
headache = validateInput(headache, 0, 10)

vomit = input("Ingrese el valor para 'vomiyos y nauseas': ")
vomit = validateInput(vomit, 0, 10)

musclePain = input("Ingrese el valor para 'dolor muscular': ")
musclePain = validateInput(musclePain, 0, 10)

fatigue = input("Ingrese el valor para 'fatiga': ")
fatigue = validateInput(fatigue, 0, 10)

congestion = input("Ingrese el valor para 'congestión nasal': ")
congestion = validateInput(congestion, 0, 10)

shivers = input("Ingrese el valor para 'escalofríos': ")
shivers = validateInput(shivers, 0, 10)

cough = input("Ingrese el valor para 'tos y dolor de garganta': ")
cough = validateInput(cough, 0, 10)

fever = input("Ingrese el valor para 'fiebre': ")
fever = validateInput(fever, 0, 10)


######################################################
######################################################

# Aplicación de reglas de inferencia
# LOS NUMEROS EN HEADACHE_LO (por ejemplo) CORRESPONDEN A LOS VALORES NITIDOS DE ENTRADA

# Regla 1: Dolor de cabeza leve Y Nauseas y vomitos leves Y Dolor muscular leve Y Fatiga leve Y Congestion nasal moderada
# Como las reglas utilizan Y se toma el minimo
rule1 = np.fmin(headache_lo[headache], np.fmin(vomit_lo[vomit], np.fmin(musclePain_lo[musclePain], np.fmin(fatigue_lo[fatigue], congestion_md[congestion]))))
# Entonces la influenza es leve
active_rule1 = np.fmin(rule1, influenza_lo)

# Regla 2: Dolor de cabeza moderado Y Nauseas y vomitos leves Y Dolor muscular moderado Y Tos moderada Y Congestion nasal severa
rule2 = np.fmin(headache_md[headache], np.fmin(vomit_lo[vomit], np.fmin(musclePain_md[musclePain], np.fmin(cough_md[cough], congestion_hi[congestion]))))
# Entonces la influenza es moderada
active_rule2 = np.fmin(rule2, influenza_md)

# Regla 3: Fiebre moderada Y Dolor de cabeza leve Y nauseas y vomitos Moderado Y Dolor muscular moderado Y fatiga moderada
#           Y escalofrios moderados Y congestion nasal severa
rule3 = np.fmin(fever_md[fever], np.fmin(headache_lo[headache], np.fmin(vomit_md[vomit], np.fmin(musclePain_md[musclePain], np.fmin(fatigue_md[fatigue], np.fmin(shivers_md[shivers], congestion_hi[congestion]))))))
# Entonces la influenza es moderada
active_rule3 = np.fmin(rule3, influenza_md)

# Regla 4: Fiebre alta Y dolor de cabeza moderado Y dolor muscular moderado Y escalofrios altos
rule4 = np.fmin(fever_hi[fever], np.fmin(headache_md[headache], np.fmin(musclePain_md[musclePain], shivers_hi[shivers])))
# Entonces la influenza es muy alta
active_rule4 = np.fmin(rule4, influenza_vhi)

# Regla 5: Dolor de cabeza moderado Y dolor muscular Alto Y fatiga moderada Y tos leve Y congestion nasal leve
rule5 = np.fmin(headache_md[headache], np.fmin(musclePain_hi[musclePain], np.fmin(fatigue_md[fatigue], np.fmin(cough_lo[cough], congestion_lo[congestion]))))
# Entonces la influenza es moderada
active_rule5 = np.fmin(rule5, influenza_md)

# Regla 6: Dolor de cabeza alto Y nauseas y vomitos alto Y dolor muscular moderado Y tos leve Y congestion nasal moderada
rule6 = np.fmin(headache_hi[headache], np.fmin(vomit_hi[vomit], np.fmin(musclePain_md[musclePain], np.fmin(cough_lo[cough], congestion_md[congestion]))))
# Entonces la influenza es alta
active_rule6 = np.fmin(rule6, influenza_hi)

######################################################
######################################################

######################################################
######################################################

# Se grafica el resultado despues de aplicar las reglas
influenza0 = np.zeros_like(x_influenza)

fig, ax0 = plt.subplots(figsize=(8, 3))

ax0.fill_between(x_influenza, influenza0, active_rule1, facecolor='b', alpha=0.7)
ax0.plot(x_influenza, influenza_lo, 'b', linewidth=0.5, linestyle='--', )
ax0.fill_between(x_influenza, influenza0, active_rule2, facecolor='g', alpha=0.7)
ax0.plot(x_influenza, influenza_md, 'g', linewidth=0.5, linestyle='--')
ax0.fill_between(x_influenza, influenza0, active_rule3, facecolor='r', alpha=0.7)
ax0.plot(x_influenza, influenza_md, 'r', linewidth=0.5, linestyle='--')
ax0.fill_between(x_influenza, influenza0, active_rule4, facecolor='c', alpha=0.7)
ax0.plot(x_influenza, influenza_vhi, 'c', linewidth=0.5, linestyle='--')
ax0.fill_between(x_influenza, influenza0, active_rule5, facecolor='m', alpha=0.7)
ax0.plot(x_influenza, influenza_md, 'm', linewidth=0.5, linestyle='--')
ax0.fill_between(x_influenza, influenza0, active_rule6, facecolor='k', alpha=0.7)
ax0.plot(x_influenza, influenza_hi, 'k', linewidth=0.5, linestyle='--')

ax0.set_title('Nivel total de influenza')

# Turn off top/right axes
for ax in (ax0,):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.show()

######################################################
######################################################

######################################################
######################################################

# Desfuzificacion
# Se agrega el resultado de todas las reglas a una variable
aggregated = np.fmax(active_rule1, np.fmax(active_rule2, np.fmax(active_rule3, np.fmax(active_rule4, np.fmax(active_rule5, active_rule6)))))

# Se calcula el centroide para desfuzificar (COA)
influenza = fuzz.defuzz(x_influenza, aggregated, 'centroide')
influenza_plot = fuzz.interp_membership(x_influenza, aggregated, influenza)  # for plot

# Se visualiza el grafico
fig, ax0 = plt.subplots(figsize=(8, 3))

ax0.plot(x_influenza, influenza_lo, 'b', linewidth=0.5, linestyle='--')
ax0.plot(x_influenza, influenza_md, 'g', linewidth=0.5, linestyle='--')
ax0.plot(x_influenza, influenza_hi, 'r', linewidth=0.5, linestyle='--')
ax0.plot(x_influenza, influenza_vhi, 'm', linewidth=0.5, linestyle='--')
ax0.fill_between(x_influenza, influenza0, aggregated, facecolor='Orange', alpha=0.7)
ax0.plot([influenza, influenza], [0, influenza_plot], 'k', linewidth=1.5, alpha=0.9)
ax0.set_title('Resultado al desfuzificar')

# Turn off top/right axes
for ax in (ax0,):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.show()

# Recolección de los datos de síntomas del paciente

