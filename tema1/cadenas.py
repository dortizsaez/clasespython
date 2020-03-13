# -*- coding: utf-8 -*-
# Las cadenas se pueden declarar de multiples formas
tipo1 = "Hola Mundo"
tipo2 = 'Hola Mundo'
tipo3 = """
    Hola Mundo,
    Tengo 2 lineas
"""
tipo4 = '''
    Hola Mundo,
    Tengo 2 lineas
'''

print tipo1
print tipo2
print tipo3
print tipo4

# Todas estas son validas

# Python tiene un problema con caracteres especiales como aquellos con tilde o que no estan contemplado en el codigo ASCII
# Para ello, hay que introducir el comentario que se encuentra en la primera linea de este codigo
tengo_tilde = 'camión'
print tengo_tilde

# Se pueden realizar muchas cosas con cadenas, como separar, contar numero de caracteres, ocurrencias en la cadenas, etc
variable = "Hola, Mundo"

# Divide la cadena de una lista separandolo por el caracter utilizado
dividir_coma = variable.split(",")
print dividir_coma

# Cuenta el numero de caracteres
n_caracteres = len(variable)
print n_caracteres

# Cuenta el numero de veces que aparece 'n' en la cadena
contar_n = variable.count("n")
print contar_n

# Indica en que posicion se encuentra 'n' dentro de la cadena
indice_n = variable.index("n")
print indice_n

mayus = variable.upper()
print mayus

minus = variable.lower()
print minus

cap = variable.title()
print cap

# Podemos concatenar 2 cadenas usando +
resultado = mayus + minus
print resultado

# Si se quiere concatenar una cadena a otra ya existente, se puede hacer asi tambien
resultado += cap
print resultado

# O unir una lista de palabras usando join
resultado = ",".join(dividir_coma)
print resultado

# Si queremos cambiar un fragmento de la cadena por otro, debemos de usar replace
reemplazo = variable.replace("Hola", "Adios")
print reemplazo

# Tambien se puede preguntar si una cadena empieza por un caracter u otra cadena
empieza_h = variable.startswith("H")
print empieza_h

# O si termina
termina_o = variable.endswith("o")
print termina_o

# Si queremos concatenar un numero a una cadena, primero convertimos el numero a texto y luego podemos concatenarlo
texto = "Son las "
numero = 5
concatena = texto + str(numero)
print concatena

# Si se quiere introducir dentro de un lugar especifico de la cadena un valor, podemos crear una plantilla indicando
# donde queremos colocarlo
plantilla = "Hola %s" % "Mundo"
print plantilla

# Gracias a esto, podemos concatenar numeros de una manera mas facil
plantilla = "Son las %s" % 5
print plantilla

# Podemos poner tantas variables como queramos, siempre que aparezca el numero correspondiente en la plantilla
plantilla = "%s %s" % ("Hola", "Gente")
print plantilla

# Y no solo eso, podemos redondear un numero flotante con un numero especifico de decimales
plantilla = "%.2f" % 5.55555
print plantilla
# Cosa que facilita mucho esta operacion si queremos obtener su valor redondeado
