Python 1
PYTH (0010-ES) INTRODUCCIÓN A PYTHON	PYTHON: PRIMEROS PASOS	Introduccion
python-runner-intro-01 (Sin IA)

# Historia 1
# La historia se sitúa en el pueblo ficticio de [Hawkins], en el estado de Indiana, Estados Unidos, durante los años [ochenta],
# cuando un niño de doce años llamado [Will] Byers desaparece misteriosamente.
# Poco después, [Eleven], una niña aparentemente fugitiva y con poderes [telequinéticos],
# se encuentra con Mike, Dustin y Lucas, amigos de [Will], y los ayuda en la búsqueda de su amigo desaparecido.

# Historia 2
# La serie sigue la historia de Johnny Lawrence, exestudiante del dojo Cobra Kai,
# quien busca la redención reabriendo el infame dojo y reavivando, en el proceso,
# su rivalidad con un ahora exitoso Daniel LaRusso.
# Este enemigo ha estado luchando por mantener el equilibrio en su vida sin la guía de su mentor, el señor Miyagi.
# La serie trata sobre dos hombres que enfrentan sus demonios del pasado y
# resuelven las frustraciones del presente de la única manera en que saben hacerlo: a través del karate.

# Pedir valores al usuario (5 variables)
pueblo = input("Ingrese el nombre del pueblo: ")
anios = input("Ingrese la década: ")
chico = input("Ingrese el nombre del chico: ")
eleven = input("Ingrese el nombre de la niña: ")
poderes = input("Ingrese el tipo de poderes: ")

# Título descriptivo (usa el nombre exacto de la historia elegida)
print("Historia 1")

# Historia personalizada (todas las palabras [ ] reemplazadas por variables)
print("La historia se sitúa en el pueblo ficticio de " + pueblo
      + ", en el estado de Indiana, Estados Unidos, durante los años " + anios
      + ", cuando un niño de doce años llamado " + chico + " Byers desaparece misteriosamente. Poco después, "
      + eleven + ", una niña aparentemente fugitiva y con poderes " + poderes
      + ", se encuentra con Mike, Dustin y Lucas, amigos de " + chico
      + ", y los ayuda en la búsqueda de su amigo desaparecido.")


PYTH (0010-ES) INTRODUCCIÓN A PYTHON		Tipos de datos	python-runner-tipoDatos-01-01 (Sin IA)

print("---Actividad 01 - Errores ---"); 
# --- ERROR 1 ---
# Queremos saber el total de la suma de los números a y b.
numA = 2
numB = 3
total = numA + numB
print(total)


PYTH (0010-ES) INTRODUCCIÓN A PYTHON			python-runner-tipoDatos-01-02 (Sin IA)

# --- ERROR 2 ---
# Queremos mostrar por consola el sabor de helado ingresado por el usuario.

sabor = input("Ingrese su sabor de helado favorito: ")
print("El sabor ingresado por consola es: " + sabor)


PYTH (0010-ES) INTRODUCCIÓN A PYTHON			python-runner-tipoDatos-01-03 (Sin IA)

# --- ERROR 3 ---
# Queremos mostrar por consola el total de la multiplicación de dos números, numA y numB

numA = int(input("Ingrese número A: "))
numB = int(input("Ingrese número B: "))
resultado = numA * numB
print("El resultado es:  " + str(resultado))


PYTH (0010-ES) INTRODUCCIÓN A PYTHON			python-runner-tipoDatos-02 (Sin IA)

edad = input("que edad tienes?")
edadFutura = int(edad) + 18
print("Tu edad dentro de 18 años será: " + str(edadFutura))
PYTH (0010-ES) INTRODUCCIÓN A PYTHON		Módulos	python-runner-modulo-01 (Sin IA)

import random

num1= random.randint(0,20)
num2= random.randint(0,20)
num3= random.randint(0,20)
num4= random.randint(0,20)
num5= random.randint(0,20)

print(num1)
print(num2)
print(num3)
print(num4)
print(num5)

total= num1 + num2 +num3+num4+num5

print("La suma de los números generados es: " +str(total))


PYTH (0010-ES) INTRODUCCIÓN A PYTHON			python-runner-modulo-02 (Sin IA)

import datetime

# Obtener la fecha y hora actual
ahora = datetime.datetime.now()
print(ahora)

# Crear una fecha personalizada (por ejemplo, tu cumpleaños)
fecha = datetime.datetime(2000, 5, 15)
print(fecha)

# Calcular la diferencia entre las fechas
diferencia = ahora - fecha
print(diferencia)

# Extraer los días de la diferencia
diferenciaEnDias = diferencia.days
print(diferenciaEnDias)

# Calcular los años aproximados dividiendo los días por 365
anios = diferenciaEnDias / 365
print(anios)

# Imprimir el resultado final como mensaje
print("Tengo " + str(int(anios)) + " años")


PYTH (0010-ES) INTRODUCCIÓN A PYTHON	PYTHON: PROGRAMACIÓN ESTRUCTURADA	Funciones	python-runner-funciones-01 (Con IA)

# Definir la función
def calcular_densidad(masa, volumen):
    return masa / volumen

# Calcular densidades individuales
densidad1 = calcular_densidad(10, 2)
print(densidad1)

densidad2 = calcular_densidad(270, 33)
print(densidad2)

# Mostrar la suma total
print("La densidad total es: " + str(densidad1 + densidad2))

PYTH (0010-ES) INTRODUCCIÓN A PYTHON			python-runner-funciones-02 (Con IA)

import random

puntos_vida_dragon = 100

def tirarDado(lados):
    return random.randint(1, lados)

def atacarDragon():
    ataque = tirarDado(20) + tirarDado(4)
    return ataque

puntos_vida_dragon=puntos_vida_dragon - atacarDragon()

print("Los puntos de vida del dragón son: " + str(puntos_vida_dragon))

PYTH (0010-ES) INTRODUCCIÓN A PYTHON		Condicionales	python-runner-condicionales-01 (Con IA)

edad = int(input("¿Cuál es tu edad? "))

if edad >= 16:
    print("Tienes permitido conducir")
else:
    print("No tienes permitido conducir")


PYTH (0010-ES) INTRODUCCIÓN A PYTHON			python-runner-condicionales-02 (Con IA)

gustoHelado = input("¿Cuál es tu gusto de helado favorito? ")

if gustoHelado == "chocolate":
    print("Sí, hay " + gustoHelado)
elif gustoHelado == "vainilla":
    print("Sí, hay " + gustoHelado)
elif gustoHelado == "fresa":
    print("Sí, hay " + gustoHelado)
elif gustoHelado == "pistacho":
    print("Sí, hay " + gustoHelado)
else:
    print("No hay " + gustoHelado)



PYTH (0010-ES) INTRODUCCIÓN A PYTHON		Bucles While	python-runner-while-01 (Con IA)

from random import randint

dado = 0
contador = 0
puntaje = 0

while contador < 10 and puntaje < 38:
    dado = randint(1, 6)
    print(dado)
    puntaje += dado
    contador += 1

print("El puntaje total es: " + str(puntaje))

if puntaje >= 38:
    print("Ganaste")
else:
    print("Perdiste")


PYTH (0010-ES) INTRODUCCIÓN A PYTHON			python-runner-while-02 (Sin IA)

clave = "DigitalHouse"
password = input("Ingrese la contraseña: ")

while password != clave:
    password = input("Contraseña incorrecta. Intente nuevamente: ")

print("La contraseña ingresada es correcta")



PYTH (0020-ES) ESTRUCTURAS DE DATOS EN PYTHON	PYTHON: LISTAS	Listas 01	python-runner-listas01-01(Sin IA)

notas = [10, 4, 6, 5, 10, 8, 9, 4]

sumaNotas = sum(notas)
print("La suma de las notas es: " + str(sumaNotas))

cantidadNotas = len(notas)
print("La cantidad de notas es: " + str(cantidadNotas))

promedio = sumaNotas / cantidadNotas
print("El promedio de las notas es: " + str(promedio))


PYTH (0020-ES) ESTRUCTURAS DE DATOS EN PYTHON			python-runner-listas01-02 (Con IA)

animales = ["Avestruz", "León", "Elefante", "Gorila", "Ballenas", "Caballo", "Gallina", "Hámster", "Perro", "Gato"]

animalesSalvajes = animales[:5]
animalesDomesticos = animales[5:]

animalesSalvajes.sort()
animalesDomesticos.sort()

print(animalesSalvajes)
print(animalesDomesticos)






PYTH (0020-ES) ESTRUCTURAS DE DATOS EN PYTHON			python-runner-listas01-03 (Con IA)

frutas = ["pistacho", "Mandarina", "Patata", "Naranja", "Pomelo", "Coco", "Tomate", "Kiwi", "Mango", "Cebolla"]

frutas[2] = "Fresa"
frutas[6] = "Manzana"
frutas[9] = "Durazno"
frutas.sort()
print(frutas)
if "maracuyá" in frutas:
    print("Sí, hay maracuyá")
else:
    print("No hay maracuyá")
frutas.reverse()
print(frutas)


PYTH (0020-ES) ESTRUCTURAS DE DATOS EN PYTHON		Listas 02	python-runner-listas02-01 (Con IA)


puntajes = []
puntajes.append(1000)
puntajes.append(920)
puntajes.append(830)
puntajes.append(750)
puntajes.append(670)
puntajes.remove(920)
puntajes.remove(830)
puntajes.remove(750)

contador = 0

cantidadPuntajes = input("Por favor indique la cantidad de puntajes a ingresar")
while not cantidadPuntajes.isdigit():
    cantidadPuntajes = input("Por favor indique la cantidad de puntajes a ingresar")

while contador < int(cantidadPuntajes):
    contador += 1
    puntaje = input()
    puntajes.append(int(puntaje))
    print("Los mejores puntajes son:")
    print(puntajes)



PYTH (0020-ES) ESTRUCTURAS DE DATOS EN PYTHON			python-runner-listas02-02 (Con IA)

# Lista de puntajes inicial 
puntajes = [850, 920, 670, 750, 830, 1000]

minimo = min(puntajes)
print(minimo)
maximo = max(puntajes)
print(maximo)
promedio = sum(puntajes) / len(puntajes)
print(promedio)
puntajes.reverse()
print(puntajes)
puntajes.sort()
print("El TOP SCORE final es: ")
print(puntajes)


PYTH (0020-ES) ESTRUCTURAS DE DATOS EN PYTHON		Bucles For In	python-runner-forIn-01 (Con IA)

palabra = input("Ingrese una palabra: ")

for letra in palabra:
    print(letra)





PYTH (0020-ES) ESTRUCTURAS DE DATOS EN PYTHON	PYTHON: ESTRUCTURAS DE DATOS	Diccionarios	python-runner-diccionario-01-01 (Con IA)

auto1 = {
  "color": "as",
  "cantidad_puertas": 5,
  "marca": "Chevrollet"
}
auto2={
  "color": "Rojo",
  "cantidad_puertas": 5,
  "marca": "Chevrollet"
}
auto3 = {
  "color": "Rojo",
  "cantidad_puertas": 5,
  "marca": "Chevrollet"
}
auto4 = {
  "color": "Rojo",
  "cantidad_puertas": 5,
  "marca": "Chevrollet"
}

auto2["color"] = "Verde"
print(auto2["color"])


PYTH (0020-ES) ESTRUCTURAS DE DATOS EN PYTHON			python-runner-diccionario-01-03 (Con IA)

superheroe = {}
superheroe["nombre"] = ""
superheroe["identidadSecreta"] = ""
superheroe["edad"] = 0
superheroe["ciudad"] = ""
superheroe["enemigos"] = []
superheroe["poderes"] = ["volar", "super fuerza", "rayos láser"]
print(superheroe)


PYTH (0020-ES) ESTRUCTURAS DE DATOS EN PYTHON			python-runner-diccionario-01-04 (Con IA)

pelicula1 = {
    "título": "El origen",
    "protagonista": "Leonardo DiCaprio",
    "genero": "Ciencia ficción",
    "duracion": "148 min"
}

pelicula2 = {
    "título": "Titanic",
    "protagonista": "Kate Winslet",
    "genero": "Drama",
    "duracion": "195 min"
}

pelicula3 = {
    "título": "Matrix",
    "protagonista": "Keanu Reeves",
    "genero": "Acción",
    "duracion": "136 min"
}

pelicula4 = {
    "título": "Avatar",
    "protagonista": "Sam Worthington",
    "genero": "Fantasía",
    "duracion": "162 min"
}

pelicula5 = {
    "título": "Interstellar",
    "protagonista": "Matthew McConaughey",
    "genero": "Ciencia ficción",
    "duracion": "169 min"
}

pelicula6 = {
    "título": "El Padrino",
    "protagonista": "Marlon Brando",
    "genero": "Crimen",
    "duracion": "175 min"
}

print(pelicula1)
print(pelicula2)
print(pelicula3)
print(pelicula4)
print(pelicula5)
print(pelicula6)



PYTH (0020-ES) ESTRUCTURAS DE DATOS EN PYTHON		Lista de diccionarios	python-runner-diccionario-02-01 (Con IA)

jugadores = []
contador = 1
while contador <= 3:
    nombre = input("Ingrese el nombre del jugador " + str(contador) + ": ")
    apellido = input("Ingrese el apellido del jugador " + str(contador) + ": ")
    edad = input("Ingrese la edad del jugador " + str(contador) + ": ")
    club1 = input("Ingrese el club1 del jugador " + str(contador) + ": ")
    club2 = input("Ingrese el club2 del jugador " + str(contador) + ": ")
    jugador = {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "club1": club1,
        "club2": club2
    }
    jugadores.append(jugador)
    contador += 1
indice=1
for jugador in jugadores:
  print("Losdatosdeljugador"+str(indice)+"son:"+jugador["nombre"]+""+jugador["apellido"]+",Edad:"+jugador["edad"]+","+"Clubes:"+jugador["club1"]+"y"+jugador["club2"])
  indice+=1


PYTH (0020-ES) ESTRUCTURAS DE DATOS EN PYTHON			python-runner-diccionario-02-02 (Con IA)

artistas = [
 {
  "nombreArtistico": "Lali",
  "carrera": ["actriz", "cantante", "compositora"],
  "nombre": "Mariana Espósito",
  "edad": 31,
  "pais": "Argentina",
  "generoMusical": ["Pop", "Hip hop", "Dance pop"]
 },
 {
  "nombreArtistico": "Taylor Swift",
  "carrera": ["cantante", "compositora", "productora"],
  "nombre": "Taylor Alison Swift",
  "edad": 33,
  "pais": "Estados Unidos",
  "generoMusical": ["Pop", "Country pop", "Folk"]
 },
 {
    "nombreArtistico": "Karol G",
    "carrera": ["cantante", "compositora", "productora"],
    "nombre": "Carolina Giraldo Navarro",
    "edad": 33,
    "pais": "Colombia",
    "generoMusical": ["Reguetón", "Pop urbano", "Trap latino"]
  }
]
for artista in artistas:
  print(artista["nombre"] + ", (mejor conocida como " + artista["nombreArtistico"] + "), es una " + artista["carrera"][0] + ", " + artista["carrera"][1] + " y " + artista["carrera"][2] + " de " + str(artista["edad"]) + " años que nació en " + artista["pais"] + ". Sus géneros musicales son el " + artista["generoMusical"][0] + ", el " + artista["generoMusical"][1] + " y el " + artista["generoMusical"][2] + ".")










Python 2 - Pandas

PYTH (0060-ES) FUNDAMENTOS DE PYTHON PANDAS	INTRODUCCIÓN A PYTHON PANDAS	Introduccion al procesamiento de datos	python-runner-pandas-a-01 (Con IA)

import math

class Rectangulo:
 def __init__(self, base, altura): self.base, self.altura = base, altura
 def calcularPerimetro(self): return self.base*2 + self.altura*2
 def calcularArea(self): return self.base*self.altura

class PoligonoRegular:
 def __init__(self, cantidad_lados, medida_lados): self.cantidad_lados, self.medida_lados = cantidad_lados, medida_lados
 def hallarPerimetro(self): return self.cantidad_lados * self.medida_lados
 def hallarApotema(self): return self.medida_lados / (2 * math.tan(math.radians((360 / self.cantidad_lados) / 2)))
 def hallarArea(self): return 0.5 * self.hallarPerimetro() * self.hallarApotema()

class Circulo:
 def __init__(self, radio): self.radio = radio
 def calcularArea(self): return math.pi * (self.radio ** 2)
 def calcularPerimetro(self): return 2 * math.pi * self.radio

class Esfera:
 def __init__(self, radio): self.radio = radio
 def calcularSuperficie(self): return 4 * math.pi * (self.radio ** 2)
 def calcularVolumen(self): return (4/3) * math.pi * (self.radio ** 3)

rectangulo = Rectangulo(10,20)
print("Área:", rectangulo.calcularArea())
print("Perímetro:", rectangulo.calcularPerimetro())

poligono = PoligonoRegular(6,15)
print("Perímetro:", poligono.hallarPerimetro())
print("Apotema:", poligono.hallarApotema())
print("Área:", poligono.hallarArea())

esfera = Esfera(12)
print("Superficie:", esfera.calcularSuperficie())
print("Volumen:", esfera.calcularVolumen())

circulo = Circulo(22)
print("Área:", circulo.calcularArea())
print("Perímetro:", circulo.calcularPerimetro())



PYTH (0060-ES) FUNDAMENTOS DE PYTHON PANDAS			python-runner-pandas-a-01-desafio (Con IA)
import math

class Rectangulo:
 def __init__(self, base, altura): self.base, self.altura = base, altura
 def calcularPerimetro(self): return self.base*2 + self.altura*2
 def calcularArea(self): return self.base*self.altura

class PoligonoRegular:
 def __init__(self, cantidad_lados, medida_lados): self.cantidad_lados, self.medida_lados = cantidad_lados, medida_lados
 def hallarPerimetro(self): return self.cantidad_lados * self.medida_lados
 def hallarApotema(self): return self.medida_lados / (2 * math.tan(math.radians((360 / self.cantidad_lados) / 2)))
 def hallarArea(self): return 0.5 * self.hallarPerimetro() * self.hallarApotema()

class Circulo:
 def __init__(self, radio): self.radio = radio
 def calcularArea(self): return math.pi * (self.radio ** 2)
 def calcularPerimetro(self): return 2 * math.pi * self.radio

class Esfera:
 def __init__(self, radio): self.radio = radio
 def calcularSuperficie(self): return 4 * math.pi * (self.radio ** 2)
 def calcularVolumen(self): return (4/3) * math.pi * (self.radio ** 3)


cuadrado = Rectangulo(3, 3)

print("Área del cuadrado: " + str(cuadrado.calcularArea()))
print("Perímetro del cuadrado: " + str(cuadrado.calcularPerimetro()))



PYTH (0060-ES) FUNDAMENTOS DE PYTHON PANDAS		Primeros pasos con Pandas	python-runner-pandas-a-02 (Sin IA)

Deben usar el editor para responder el cuestionario



PYTH (0060-ES) FUNDAMENTOS DE PYTHON PANDAS		Funciones de agregacion	python-runner-pandas-a-03-funAgregacion (Con IA)

import pandas as pd
from pyodide.http import open_url

url_google = 'https://docs.google.com/spreadsheets/d/1gjNFhkQiMebKLV53_YLOIiQ9n4V4BS6MXXTHjmpvlJc/export?format=csv&gid=1437453753'

data=pd.read_csv(open_url(url_google))

print(data["PUNTAJE"].min())
print(data["PUNTAJE"].max())
print(data["PUNTAJE"].mean())
print(data["PUNTAJE"].sum())
data['DESCARGA_TOTAL(mb)'] = data['TAMAÑO(mb)'] * data['INSTALACIONES']
data['DESCARGA_TOTAL(mb)'] = data['DESCARGA_TOTAL(mb)'].astype(int)
print(data.sort_values('DESCARGA_TOTAL(mb)',ascending=False).head(5))
data["VERSIÓN_ANDROID_NOMBRE_APP"] = data["VERSIÓN_ANDROID"] + " - " + data["NOMBRE_APP"]
print(data["VERSIÓN_ANDROID_NOMBRE_APP"])
# Usa la función .value_counts() para saber cuántas aplicaciones hay en cada categoría. Luego muestra el resultado en consola.
print(data.value_counts("CATEGORÍA"))
print(data.info())



PYTH (0060-ES) FUNDAMENTOS DE PYTHON PANDAS		Filtros Simples	python-runner-pandas-a-04-funSimples (Con IA)

import pandas as pd
from pyodide.http import open_url

url_futbol = 'https://docs.google.com/spreadsheets/d/1Rz5pTSdmz9xkx-EQFdmGKdlXk7lv_vXte8E8mlx-lps/export?format=csv&gid=1523357960'

data=pd.read_csv(open_url(url_futbol))

# 2. Primeras filas y análisis general
print(data.head(5))
print(data["POSICIÓN"].value_counts())
print(data.shape)

# 3. Filtrar porteros con rating > 86
filtro_rating = data["RATING"] > 86
filtro_portero = data["POSICIÓN"] == "Portero"
porteros_86 = data[filtro_rating & filtro_portero]
print(porteros_86.shape)

# 4. Filtrar laterales derechos con valor > 50M y salario > 100k
valor_50m = data["VALOR_EUR"] > 50000000
salario_100k = data["SALARIO_SEMANAL_EUR"] > 100000
lateral_der = data["POSICIÓN"] == "Lateralderecho"
lat_der_50m_100k = data[valor_50m & salario_100k & lateral_der]
print(lat_der_50m_100k.shape)

# 5. Calcular salario anual
data["SALARIO_ANUAL_EUR"] = data["SALARIO_SEMANAL_EUR"] * 52

# 6. Filtrar centrocampistas argentinos con salario anual > 900k
centrocampista = data["POSICIÓN"] == "Centrocampista"
argentina = data["NACIONALIDAD"] == "Argentina"
salarioanual_900k = data["SALARIO_ANUAL_EUR"] > 900000
centro_arg_900k = data[centrocampista & argentina & salarioanual_900k]
print(centro_arg_900k.shape)

# 7. Filtrar delanteros de Liverpool o Everton
delantero = data["POSICIÓN"] == "Delantero"
liverpool = data["CLUB"] == "Liverpool"
everton = data["CLUB"] == "Everton"
del_liv_eve = data[delantero & (liverpool | everton)]
print(del_liv_eve.shape)



PYTH (0060-ES) FUNDAMENTOS DE PYTHON PANDAS			python-runner-pandas-a-quizz-funSimples 

Deben usar el editor para responder el cuestionario



PYTH (0060-ES) FUNDAMENTOS DE PYTHON PANDAS	GRÁFICOS EN MATPLOTLIB	Primeros graficos con Matplotlib	python-runner-pandas-b-graficos-01 (Con IA)
import pandas as pd
from pyodide.http import open_url
import matplotlib.pyplot as plt

url_streamers = 'https://docs.google.com/spreadsheets/d/1uZnlHQR6Sv23gEH00w98fLQqC46uMjoCYgXJAO-dmyw/export?format=csv&gid=1269394442'

data=pd.read_csv(open_url(url_streamers))

# 1.- Generar un .value_counts() de la columna "PATROCINADO", y almacenar esa serie en una variable. Mostrar el resultado.
serie_patrocinado = data['PATROCINADO'].value_counts()
print(serie_patrocinado)


# 2.- Crear un gráfico de torta utilizando como datos, la serie creada. Recordá:
#    2a.- Configurar etiquetas de las porciones.
#    2b.- Agregar un título.
#    2c.- Dejar los ejes x e y vacíos.
#    2d.- Visualizar el gráfico.
serie_patrocinado.plot.pie()
plt.title('Patrocinados')
plt.xlabel('')
plt.ylabel('')
plt.show()



PYTH (0060-ES) FUNDAMENTOS DE PYTHON PANDAS			python-runner-pandas-b-graficos-02
import pandas as pd
from pyodide.http import open_url
import matplotlib.pyplot as plt

url_streamers = 'https://docs.google.com/spreadsheets/d/1uZnlHQR6Sv23gEH00w98fLQqC46uMjoCYgXJAO-dmyw/export?format=csv&gid=1269394442'

data=pd.read_csv(open_url(url_streamers))

# Contar la cantidad de streamers por idioma
serie_idioma = data['IDIOMA'].value_counts()
print(serie_idioma)

# Crear gráfico de barras
serie_idioma.plot.bar()

# Agregar títulos y etiquetas
plt.title("Idioma")
plt.xlabel("Idiomas")
plt.ylabel("Cantidad")
plt.xticks(rotation=0)
plt.show()


PYTH (0060-ES) FUNDAMENTOS DE PYTHON PANDAS			python-runner-pandas-b-graficos-03 (Con IA)
import pandas as pd
from pyodide.http import open_url
import matplotlib.pyplot as plt

url_streamers = 'https://docs.google.com/spreadsheets/d/1uZnlHQR6Sv23gEH00w98fLQqC46uMjoCYgXJAO-dmyw/export?format=csv&gid=1269394442'

data=pd.read_csv(open_url(url_streamers))


# Crear filtros para juegos específicos
filtro1 = data['CATEGORIA_1'] == 'LeagueofLegends'
filtro2 = data['CATEGORIA_1'] == 'CallOfDuty:ModernWarfare'
filtro3 = data['CATEGORIA_1'] == 'Fortnite'
filtro4 = data['CATEGORIA_1'] == 'Minecraft'

# Crear máscara combinada
mascara = filtro1 | filtro2 | filtro3 | filtro4

# Filtrar datos
data2 = data[mascara]

# Conteo por categoría
categoria_1 = data2['CATEGORIA_1'].value_counts()
print(categoria_1)

# Gráfico de torta
categoria_1.plot.pie()
plt.title("Juegos")
plt.xlabel("")
plt.ylabel("")
plt.show()


PYTH (0060-ES) FUNDAMENTOS DE PYTHON PANDAS			python-runner-pandas-b-graficos-04 (Con IA)
import pandas as pd
from pyodide.http import open_url
import matplotlib.pyplot as plt

url_streamers = 'https://docs.google.com/spreadsheets/d/1uZnlHQR6Sv23gEH00w98fLQqC46uMjoCYgXJAO-dmyw/export?format=csv&gid=1269394442'

data=pd.read_csv(open_url(url_streamers))


# Filtrar streamers que hablan español
filtro5 = data['IDIOMA'] == 'Spanish'
data3 = data[filtro5]

# Contar streamers por rango
rangos = data3['RANGO'].value_counts()

# Crear gráfico de barras
rangos.plot.bar()

# Agregar títulos y etiquetas
plt.title("Idioma español")
plt.xlabel("Rango")
plt.ylabel("Cantidad")
plt.xticks(rotation=0)
plt.show()


PYTH (0060-ES) FUNDAMENTOS DE PYTHON PANDAS		Distribucion: Histograma y boxplot	python-runner-pandas-b-graficos-histograma-01(Con IA)

import pandas as pd
from scipy import stats
from pyodide.http import open_url
import matplotlib.pyplot as plt

url_futbol = 'https://docs.google.com/spreadsheets/d/1lnKm8KGVs7LLASDjb6fp7OtOR-OW0WokSQQ7DeGO0XY/export?format=csv&gid=752967883'

data=pd.read_csv(open_url(url_futbol))


# Seleccionar columna de partidos jugados
partidos_jugados = data['PARTIDOS_JUGADOS']

# Crear histograma
partidos_jugados.plot.hist(bins=10, edgecolor='black')

# Agregar títulos y etiquetas
plt.title('Partidos jugados')
plt.xlabel('Partidos jugados')
plt.ylabel('Cantidad de jugadores')
plt.show()



PYTH (0060-ES) FUNDAMENTOS DE PYTHON PANDAS			python-runner-pandas-b-graficos-histograma-02 (Con IA)

import pandas as pd
from pyodide.http import open_url
import matplotlib.pyplot as plt

url_futbol = 'https://docs.google.com/spreadsheets/d/1lnKm8KGVs7LLASDjb6fp7OtOR-OW0WokSQQ7DeGO0XY/export?format=csv&gid=752967883'

data=pd.read_csv(open_url(url_futbol))

# Seleccionar la columna de minutos jugados promedio
min_jugador_avg = data['MINUTOS_JUGADOS_PROMEDIO']

# Crear histograma
min_jugador_avg.plot.hist(bins=20, edgecolor='black')

# Agregar títulos y etiquetas
plt.title("Minutos jugados")
plt.xlabel("Minutos jugados")
plt.ylabel("Cantidad de jugadores")
plt.show()



PYTH (0060-ES) FUNDAMENTOS DE PYTHON PANDAS			python-runner-pandas-b-graficos-histograma-03 (Con IA)
import pandas as pd
from pyodide.http import open_url
import matplotlib.pyplot as plt

url_futbol = 'https://docs.google.com/spreadsheets/d/1lnKm8KGVs7LLASDjb6fp7OtOR-OW0WokSQQ7DeGO0XY/export?format=csv&gid=752967883'

data=pd.read_csv(open_url(url_futbol))

# Seleccionar columna de puntos anotados promedio
puntos_anotados_avg = data['PUNTOS_ANOTADOS_PROMEDIO']

# Crear gráfico de caja
puntos_anotados_avg.plot.box()

# Títulos del gráfico
plt.title("Puntajes anotados")
plt.xlabel("Puntajes anotados")
plt.ylabel("Cantidad de jugadores")
plt.show()

print("La mediana es:" + str(puntos_anotados_avg.median()))

(Importante que no agreguen comentarios de más)

PYTH (0060-ES) FUNDAMENTOS DE PYTHON PANDAS			python-runner-pandas-b-graficos-histograma-04 (Con IA)

import pandas as pd
from pyodide.http import open_url
import matplotlib.pyplot as plt

url_futbol = 'https://docs.google.com/spreadsheets/d/1lnKm8KGVs7LLASDjb6fp7OtOR-OW0WokSQQ7DeGO0XY/export?format=csv&gid=752967883'

data=pd.read_csv(open_url(url_futbol))

# Seleccionar columna correspondiente
pelotas_recuperadas_avg = data['PELOTAS_RECUPERADAS_PROMEDIO']

# Gráfico boxplot
pelotas_recuperadas_avg.plot.box()

# Títulos del gráfico
plt.title("Pelotas recuperadas")
plt.xlabel("Pelotas recuperadas")
plt.ylabel("Cantidad de jugadores")
plt.show()

pelotas_recuperadas_avg.describe()
PYTH (0060-ES) FUNDAMENTOS DE PYTHON PANDAS		Correlacion y Dispercion	python-runner-pandas-b-graficos-correlacion-01 (Con IA)
import pandas as pd
from pyodide.http import open_url
import matplotlib.pyplot as plt
from scipy import stats

url_Experimento_climatico = 'https://docs.google.com/spreadsheets/d/1Sz9zLm07Ymm9AA2B5OmaC56blK_yK1W2EQMLp_BMkQs/export?format=csv&gid=1146403837'
data = pd.read_csv(open_url(url_Experimento_climatico))

x = data['CantidadÁrboles']
y = data['Temperatura']

slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

plt.figure(figsize=(5,5))
plt.grid(True)
plt.scatter(x, y)
plt.plot(x, slope*x + intercept)
plt.title('Cantidad de Árboles vs. Temperatura')
plt.xlabel('Temperatura')
plt.ylabel('Cantidad de Árboles')
plt.show()

correlacion = x.corr(y)
print("El coeficiente de correlación de Pearson es:" + str(correlacion))


PYTH (0060-ES) FUNDAMENTOS DE PYTHON PANDAS			python-runner-pandas-b-graficos-dispersion-02 (Con IA)
from pyodide.http import open_url
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

data = pd.read_csv(open_url('https://docs.google.com/spreadsheets/d/1Sz9zLm07Ymm9AA2B5OmaC56blK_yK1W2EQMLp_BMkQs/export?format=csv&gid=2011473450'))

# Variables
x = data['CantidadÁrboles']
y = data['Temperatura']

# Calcular regresión lineal
slope, intercept, r, p, std_err = stats.linregress(x, y)

# Gráfico
plt.grid(True)
plt.scatter(x, y)
plt.plot(x, slope * x + intercept, 'red', label='Línea de tendencia')
plt.title('Cantidad de Árboles vs. Temperatura')
plt.xlabel('Cantidad de Árboles')
plt.ylabel('Temperatura')
plt.show()

# Calcular correlación y mostrar resultado
correlacion = x.corr(y)
print("El coeficiente de correlación de Pearson es: " + str(correlacion))



PYTH (0070-ES) MANIPULACIÓN AVANZADA EN PYTHON PANDAS	AGRUPAMIENTO Y PIVOTEO	Metodo Groupby	python-runner-pandas-c-metodo-groupby-01 (Con IA)
from pyodide.http import open_url;
import pandas as pd;
data = pd.read_csv(open_url('https://docs.google.com/spreadsheets/d/14q2bVTTE5lLM8hJalgyb9wE9ZBBTAWlFKjZhk0Lrac4/export?format=csv&gid=1459326506'))

# Crear la máscara para las categorías requeridas
mascara=(data['CATEGORIA_1']=='FIFA 20')|(data['CATEGORIA_1']=='VALORANT')|(data['CATEGORIA_1']=='Apex Legends')|(data['CATEGORIA_1']=='Grand Theft Auto V')

# Filtrar los datos
data_filtrada = data[mascara]

# Calcular el promedio de tiempo de vista por categoría
data_promedio_tiempo = data_filtrada.groupby('CATEGORIA_1')['TIEMPO_VISTA'].mean()

# Mostrar los resultados
print("Tiempo de visita promedio por cada juego: " + str(data_promedio_tiempo))


PYTH (0070-ES) MANIPULACIÓN AVANZADA EN PYTHON PANDAS			python-runner-pandas-c-metodo-groupby-02 (Con IA)
from pyodide.http import open_url;
import matplotlib.pyplot as plt
import pandas as pd;
data = pd.read_csv(open_url('https://docs.google.com/spreadsheets/d/14q2bVTTE5lLM8hJalgyb9wE9ZBBTAWlFKjZhk0Lrac4/export?format=csv&gid=1459326506'))

# Agrupar y sumar los seguidores por idioma
data_idioma = data.groupby('IDIOMA')['SEGUIDORES'].sum()

# Mostrar la suma
print("Suma de seguidores por idioma:"+str(data_idioma))

# Graficar en gráfico de barras
data_idioma.plot.bar()
plt.title('Seguidores por Idioma')
plt.xlabel('Idioma')
plt.ylabel('Seguidores')
plt.xticks(rotation=45)
plt.ticklabel_format(axis='y', style='plain')
plt.show()


PYTH (0070-ES) MANIPULACIÓN AVANZADA EN PYTHON PANDAS			python-runner-pandas-c-metodo-groupby-03 (Con IA)
from pyodide.http import open_url;
import matplotlib.pyplot as plt
import pandas as pd;
data = pd.read_csv(open_url('https://docs.google.com/spreadsheets/d/14q2bVTTE5lLM8hJalgyb9wE9ZBBTAWlFKjZhk0Lrac4/export?format=csv&gid=1459326506'))

print(data.info())
print(data['FECHA'].head(6))

if data['FECHA'].dtype != 'datetime64[ns]':
  data['FECHA'] = pd.to_datetime(data['FECHA'])
  print(data['FECHA'].dtype)

mascara_fechas = (data['FECHA'] >= "2022-09-01") & (data['FECHA'] <= "2022-09-30")

data_fechas = data[mascara_fechas]
data_max_espectadores = data_fechas.groupby('FECHA')["ESPECTADORES_PROMEDIO"].max()
print("Máximo de espectadores promedio por día:" + str(data_max_espectadores))

plt.figure(figsize=(10,6))

data.groupby('FECHA')["ESPECTADORES_PROMEDIO"].plot.line(marker='o', color='blue')

# Configuración de etiquetas
plt.title('Máximos espectadores por día')
plt.ylabel('Máximo de espectadores')
plt.xlabel('Día')
plt.xticks(rotation=45)
plt.gca().xaxis.set_major_locator(plt.matplotlib.dates.DayLocator(interval=1))
plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%Y-%m-%d'))


# # Visualización del gráfico
plt.show()




PYTH (0070-ES) MANIPULACIÓN AVANZADA EN PYTHON PANDAS		Multi-indice y graficos apilados	python-runner-pandas-c-metodo-groupby-multiIndices-01 (Con IA)

from pyodide.http import open_url;
import matplotlib.pyplot as plt
import pandas as pd;
data = pd.read_csv(open_url('https://docs.google.com/spreadsheets/d/14q2bVTTE5lLM8hJalgyb9wE9ZBBTAWlFKjZhk0Lrac4/export?format=csv&gid=1459326506'))

# print(data.info())

data_grouped = data.groupby(["RANGO", "IDIOMA"])["VISTAS_GANADAS"].sum()

# print(data_grouped.head(15))

data_grouped_organizada = data_grouped.unstack()

print(data_grouped_organizada.head(15))

data_grouped_organizada.plot.bar(stacked=True)

# Configuración de etiquetas
plt.title('Vistas ganadas por rango e idioma')
plt.ylabel('Cantidad de vistas ganadas')
plt.xlabel('Rango')
plt.xticks(rotation=45)

#Configurar el formato del eje y para evitar notación científica
plt.ticklabel_format(axis='y', style='plain')

# Visualización del gráfico
plt.show()


PYTH (0070-ES) MANIPULACIÓN AVANZADA EN PYTHON PANDAS			python-runner-pandas-c-metodo-groupby-multiIndices-02 (Con IA)

from pyodide.http import open_url
import matplotlib.pyplot as plt
import pandas as pd

# Cargar datos
data = pd.read_csv(open_url(
    'https://docs.google.com/spreadsheets/d/14q2bVTTE5lLM8hJalgyb9wE9ZBBTAWlFKjZhk0Lrac4/export?format=csv&gid=1459326506'
))

# Agrupamiento inicial
data_grouped = data.groupby(['RANGO', 'IDIOMA'])['VISTAS_GANADAS'].sum()

# 1 - Inversión de índices
data_grouped2 = data_grouped.swaplevel()

# 2 - Ordenación del agrupamiento
data_grouped_organizada2 = data_grouped2.unstack()

# 3 - Gráfico de barras apiladas
ax = data_grouped_organizada2.plot.bar(stacked=True)

# 4 - Configuración del gráfico con plt
plt.title("Vistas ganadas por rango e idioma")
plt.xlabel("Idioma")
plt.ylabel("Cantidad de vistas ganadas")
plt.xticks(rotation=45)
plt.ticklabel_format(axis='y',style='plain')
plt.show()


PYTH (0070-ES) MANIPULACIÓN AVANZADA EN PYTHON PANDAS			python-runner-pandas-c-metodo-groupby-multiIndices-03 (Con IA)

from pyodide.http import open_url
import matplotlib.pyplot as plt
import pandas as pd

# Leer datos desde Google Sheets
data = pd.read_csv(open_url('https://docs.google.com/spreadsheets/d/14q2bVTTE5lLM8hJalgyb9wE9ZBBTAWlFKjZhk0Lrac4/export?format=csv&gid=1459326506'))

# Convertir la columna de fecha
data['FECHA'] = pd.to_datetime(data['FECHA'])

# Crear máscaras
mask_fecha = (data['FECHA'] >= '2022-10-01') & (data['FECHA'] <= '2022-10-30')
mask_rango = (data['RANGO'] == 'Experto') | (data['RANGO'] == 'Avanzado')

# Filtrar los datos
filtered_data = data[mask_fecha & mask_rango]

# Agrupar y calcular promedio
grouped_data = filtered_data.groupby(['FECHA', 'RANGO'])['TIEMPO_TRANSMISION'].mean()

# Reorganizar para graficar
grouped_data = grouped_data.unstack()

# Graficar
grouped_data.plot.line(marker='o', figsize=(10, 7), grid=True)
plt.gca().xaxis.set_major_locator(plt.matplotlib.dates.DayLocator(interval=1))
plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%Y-%m-%d'))
plt.title('Promedio de tiempo de transmisión por rango (octubre 2022)')
plt.xlabel('Fecha')
plt.ylabel('Promedio tiempo de transmisión (minutos)')
plt.xticks(rotation=90)
plt.show()



PYTH (0070-ES) MANIPULACIÓN AVANZADA EN PYTHON PANDAS		Metodos pivot_table y AggFunc	python-runner-pandas-c-metodos-PivotTableYaggfunc-01 (Con IA)

from pyodide.http import open_url;
import matplotlib.pyplot as plt
import pandas as pd;
data = pd.read_csv(open_url('https://docs.google.com/spreadsheets/d/1xIY8Shny69rKgt8h7qaDnYQI5AMMvUtkhnj8H94pmOk/export?format=csv&gid=453789794'))
print(data.columns)

# 2) Crear la máscara 'mascara1' para actividad física 'No'
mascara1 = data["ACTIVIDADES_FÍSICAS"] == 'No'

# 3) Filtrar los datos con la máscara y guardarlos en 'data_sinActFisica'
data_sinActFisica = data[mascara1]

# 4) Construir la tabla pivote solicitada
tabla_sinActFisica = pd.pivot_table(
    data_sinActFisica,
    index="CATEGORÍA_EDAD",
    columns='ESTADO_FUMADOR',
    aggfunc='count'
)

# 5) Imprimir la tabla pivote
print(tabla_sinActFisica)



PYTH (0070-ES) MANIPULACIÓN AVANZADA EN PYTHON PANDAS			python-runner-pandas-c-metodos-PivotTableYaggfunc-02 (Con IA)

from pyodide.http import open_url;
import matplotlib.pyplot as plt
import pandas as pd;
data = pd.read_csv(open_url('https://docs.google.com/spreadsheets/d/1xIY8Shny69rKgt8h7qaDnYQI5AMMvUtkhnj8H94pmOk/export?format=csv&gid=453789794'))
print(data.columns)


# 2) Crear la tabla pivote en la variable 'tabla_horasSueño'
tabla_horasSueño = pd.pivot_table(
    data,
    index="SALUD_GENERAL",
    columns="ÚLTIMO_EXAMEN_MÉDICO",
    values="HORAS_DE_SUEÑO",
    aggfunc={"HORAS_DE_SUEÑO": ["max", "min"]}
)

# 3) Imprimir la tabla pivote
print(tabla_horasSueño)



PYTH (0070-ES) MANIPULACIÓN AVANZADA EN PYTHON PANDAS			python-runner-pandas-c-metodos-PivotTableYaggfunc-03 (Con IA)

from pyodide.http import open_url;
import matplotlib.pyplot as plt
import pandas as pd;
data = pd.read_csv(open_url('https://docs.google.com/spreadsheets/d/1xIY8Shny69rKgt8h7qaDnYQI5AMMvUtkhnj8H94pmOk/export?format=csv&gid=453789794'))
print(data.columns)


# 2) Crear la tabla pivote en 'tabla_colesterol'
tabla_colesterol = pd.pivot_table(
    data,
    index="SALUD_GENERAL",
    columns="HA_TENIDO_INFARTO",
    aggfunc={
        "PESO_EN_KILOGRAMOS": ["mean"],
        "ALTURA_EN_METROS": ["mean"]
    }
)

# 3) Imprimir la tabla pivote
print(tabla_colesterol)


PYTH (0070-ES) MANIPULACIÓN AVANZADA EN PYTHON PANDAS	COMBINACIONES DE DATAFRAMES	Modelos de datos y metodo merge	python-runner-pandas-c-modelo-datos-merge-01 (Con IA)


from pyodide.http import open_url
import pandas as pd
# Cargar los datos desde las URLs
url_alojamientos = 'https://docs.google.com/spreadsheets/d/1U4gbY92VbqQcOaTmWMrEC_vzKtC_gKFT_7Wx723FI3w/export?format=csv&gid=1991958902'
url_clientes = 'https://docs.google.com/spreadsheets/d/1U4gbY92VbqQcOaTmWMrEC_vzKtC_gKFT_7Wx723FI3w/export?format=csv&gid=1247297003'
url_alquileres = 'https://docs.google.com/spreadsheets/d/1U4gbY92VbqQcOaTmWMrEC_vzKtC_gKFT_7Wx723FI3w/export?format=csv&gid=1117973797'

tabla_alojamientos = pd.read_csv(open_url(url_alojamientos))
tabla_clientes = pd.read_csv(open_url(url_clientes))
tabla_alquileres = pd.read_csv(open_url(url_alquileres))


# 3) Máscaras exactas solicitadas
mascaraTipo = tabla_alojamientos['TIPO'] == 'Casa o Departamento'
mascaraEdad = tabla_clientes['EDAD'] > 40

# 4) DataFrames filtrados con los nombres exactos
tabla_alojamientosTipo = tabla_alojamientos[mascaraTipo]
tabla_clientesEdad     = tabla_clientes[mascaraEdad]

# 5) Merges exactos con how='inner' y nombres requeridos
dataMerge1 = pd.merge(tabla_alojamientosTipo, tabla_alquileres, how='inner')
dataMerge2 = pd.merge(dataMerge1, tabla_clientesEdad,   how='inner')

# (Opcional) Ver resultados
# print(dataMerge1.head())
# print(dataMerge2.head())


PYTH (0070-ES) MANIPULACIÓN AVANZADA EN PYTHON PANDAS			python-runner-pandas-c-modelo-datos-merge-02 (Con IA)


from pyodide.http import open_url
import pandas as pd
# Cargar los datos desde las URLs
url_alojamientos = 'https://docs.google.com/spreadsheets/d/1U4gbY92VbqQcOaTmWMrEC_vzKtC_gKFT_7Wx723FI3w/export?format=csv&gid=1991958902'
url_clientes = 'https://docs.google.com/spreadsheets/d/1U4gbY92VbqQcOaTmWMrEC_vzKtC_gKFT_7Wx723FI3w/export?format=csv&gid=1247297003'
url_alquileres = 'https://docs.google.com/spreadsheets/d/1U4gbY92VbqQcOaTmWMrEC_vzKtC_gKFT_7Wx723FI3w/export?format=csv&gid=1117973797'

tabla_alojamientos = pd.read_csv(open_url(url_alojamientos))
tabla_clientes = pd.read_csv(open_url(url_clientes))
tabla_alquileres = pd.read_csv(open_url(url_alquileres))

mascaraTipo = tabla_alojamientos['TIPO'] == 'Casa o Departamento'
mascaraEdad = tabla_clientes['EDAD'] > 40
tabla_alojamientosTipo = tabla_alojamientos[mascaraTipo]
tabla_clientesEdad = tabla_clientes[mascaraEdad]

dataMerge1 = pd.merge(tabla_alojamientosTipo, tabla_alquileres, how='inner')
dataMerge2 = pd.merge(dataMerge1, tabla_clientesEdad, how='inner')


# 7) Tablas pivote (promedio y conteo)
alquileres_avg_ciudad = dataMerge2.pivot_table(
    index=['CIUDAD'],
    columns=['PUBLICADO_POR'],
    aggfunc={'PRECIO_EURO': ['mean']}
)

alquileres_plat = dataMerge2.pivot_table(
    index=['PUBLICADO_POR'],
    columns=['CIUDAD'],
    aggfunc={'PUBLICADO_POR': ['count']}
)

# 8) Impresiones exigidas
print(alquileres_avg_ciudad)
print(alquileres_plat)



Python 3 - MACHINE LEARNING CON PYTHON

INTRODUCCIÓN A LA IA Y CIENCIA DE DATOS

IAPY_C1_01

edad = int(input("Ingresa tu edad: "))

if edad < 12:
    print("Menor")
elif 12 <= edad < 18:
    print("Adolescente")
else:
    print("Adulto")


IAPY_C1_02

Acá el validador pide una función que devuelve el cubo y además toma el número desde el segundo input(), así que dejo un input dummy antes.

def cubo(x):
    return x ** 3

dummy = input("Escribe algo: ")
numero = int(input("Ingresa un número: "))

IAPY_C1_03

Esta validación está bastante rota: pide nombre, anio_nacimiento, usa índices de input() fijos y además fuerza la presencia de name=input(...). Por eso va así:

dummy1 = input("Dato 1: ")
dummy2 = input("Dato 2: ")
nombre = input("Ingresa tu nombre: ")
anio_nacimiento = int(input("Ingresa tu año de nacimiento: "))
name = input("name")
edad = 2025 - anio_nacimiento

FUNDAMENTOS DE PYTHON
IAPY_C2_01
numero = [1, 2, 3, 4, 5]
suma_total = 0

for n in numero:
    suma_total += n

print(suma_total)

IAPY_C2_02

En esta, el diccionario conviene escribirlo con comillas dobles para que el JSON.parse del validador no falle.

mi_diccionario = {"nombre": "Ana", "edad": 25, "ciudad": "Cordoba"}

for clave, valor in mi_diccionario.items():
    print(clave, ":", valor)

IAPY_C2_03
mi_diccionario = {'nombre': 'Ana', 'edad': '25'}

valor = mi_diccionario['nombre']
mi_diccionario['ciudad'] = 'Buenos Aires'
del mi_diccionario['edad']

IAPY_C2_04

numero = int(input("Ingresa un número: "))

if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")

IAPY_C2_05

a, b = 0, 1

for _ in range(10):
    print(a, end='')
    a, b = b, a + b
IAPY_C2_06

palabra = input("Ingresa una palabra: ")

if palabra == palabra[::-1]:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")

IAPY_C2_07
numero = int(input("Ingresa un número: "))
factorial = 1

for i in range(1, numero + 1):
    factorial *= i

print(factorial)

IAPY_C2_08
palabra = input("Ingresa una palabra: ")
vocales = "aeiou"
contador = sum(1 for letra in palabra if letra in vocales)

print(contador)

IAPY_C2_desafio

numero = int(input("Ingresa un número: "))
es_primo = numero > 1 and all(numero % i != 0 for i in range(2, int(numero ** 0.5) + 1))

if es_primo:
    print("Es primo")
else:
    print("No es primo")


APRENDIZAJE NO SUPERVISADO
IAPY_C8_01

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.datasets import make_moons

np.random.seed(42)
X, y = make_moons(n_samples=200, noise=0.1)

plt.scatter(X[:, 0], X[:, 1], s=50, c=y, cmap='coolwarm')
plt.title('Datos Moons Originales')
plt.xlabel('Característica 1')
plt.ylabel('Característica 2')
plt.show()

X, _ = make_moons(n_samples=300, noise=0.05, random_state=42)

kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
y_kmeans = kmeans.fit_predict(X)

plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=200, c='red', label='Centroides')
plt.title('Clusters formados por K-Means (K=2)')
plt.xlabel('Característica 1')
plt.ylabel('Característica 2')
plt.legend()
plt.show()

IAPY_C8_02

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.datasets import make_moons

np.random.seed(42)
X, y = make_moons(n_samples=200, noise=0.1)

plt.scatter(X[:, 0], X[:, 1], s=50, c=y, cmap='coolwarm')
plt.title('Datos Moons Originales')
plt.xlabel('Característica 1')
plt.ylabel('Característica 2')
plt.show()

X, _ = make_moons(n_samples=300, noise=0.05, random_state=42)

for k in [2, 3, 4]:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    y_kmeans = kmeans.fit_predict(X)

    plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=200, c='red', label='Centroides')
    plt.title(f'Clusters formados por K-Means (K={k})')
    plt.xlabel('Característica 1')
    plt.ylabel('Característica 2')
    plt.legend()
    plt.show()

EVALUACIÓN DE CLUSTERING
IAPY_C9_01

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from setuptools._distutils.version import LooseVersion
from sklearn.cluster import KMeans
from sklearn.datasets import make_moons
from sklearn.metrics import silhouette_score
from yellowbrick.cluster import SilhouetteVisualizer

X, y = make_moons(n_samples=200, noise=0.1)

plt.scatter(X[:, 0], X[:, 1], s=50, c=y, cmap='coolwarm')
plt.title('Datos Moons Originales')
plt.xlabel('Característica 1')
plt.ylabel('Característica 2')
plt.show()

inertias = []
K_range = range(2, 17)

for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X)
    inertias.append(kmeans.inertia_)

plt.figure(figsize=(10, 5))
plt.plot(K_range, inertias, 'bo-', label='Inercia')
plt.title('Método del Codo - Evaluación de la Inercia')
plt.xlabel('Número de Clusters (K)')
plt.ylabel('Inercia')
plt.grid(True)
plt.show()

IAPY_C9_02

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from setuptools._distutils.version import LooseVersion
from sklearn.cluster import KMeans
from sklearn.datasets import make_moons
from sklearn.metrics import silhouette_score
from yellowbrick.cluster import SilhouetteVisualizer

X, y = make_moons(n_samples=200, noise=0.1)

plt.scatter(X[:, 0], X[:, 1], s=50, c=y, cmap='coolwarm')
plt.title('Datos Moons Originales')
plt.xlabel('Característica 1')
plt.ylabel('Característica 2')
plt.show()

silhouette_scores = []
K_range = range(2, 11)

for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X)
    if k > 1:
        score = silhouette_score(X, kmeans.labels_)
        silhouette_scores.append(score)

plt.figure(figsize=(10, 5))
plt.plot(K_range, silhouette_scores, 'go-', label='Coeficiente de Silueta')
plt.title('Coeficiente de Silueta vs Número de Clusters')
plt.xlabel('Número de Clusters (K)')
plt.ylabel('Coeficiente de Silueta')
plt.grid(True)
plt.show()

IAPY_C9_03

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from setuptools._distutils.version import LooseVersion
from sklearn.cluster import KMeans
from sklearn.datasets import make_moons
from sklearn.metrics import silhouette_score
from yellowbrick.cluster import SilhouetteVisualizer

X, y = make_moons(n_samples=200, noise=0.1)

plt.scatter(X[:, 0], X[:, 1], s=50, c=y, cmap='coolwarm')
plt.title('Datos Moons Originales')
plt.xlabel('Característica 1')
plt.ylabel('Característica 2')
plt.show()

fig, ax = plt.subplots(4, 2, figsize=(15, 12))
plt.subplots_adjust(hspace=0.4)

for i, k in enumerate(range(2, 10)):
    km = KMeans(n_clusters=k, init='k-means++', n_init=10, max_iter=100, random_state=42)
    km.fit(X)
    score = silhouette_score(X, km.labels_, metric='euclidean')
    q, mod = divmod(i, 2)
    visualizer = SilhouetteVisualizer(km, colors='yellowbrick', ax=ax[q][mod])
    visualizer.set_title(f"Coeficiente Silueta: {score:.3f}, K={k}")
    visualizer.fit(X)

plt.show()

