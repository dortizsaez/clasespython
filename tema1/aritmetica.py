# Python actua como si fuera una calculadora, por lo que respeta las reglas matematicas de la aritmetica
# Se debe de seguir las reglas de prioridad de operaciones
# 1. Parentesis
# 2. Potencias y raices
# 3. Multiplicaciones y divisiones
# 4. Sumas y restas
# Por lo que si queremos obtener el valor correcto, debemos tener esto en cuenta

# Esta operacion realizara primero la mutliplicacion, y luego las sumas de izquierda a derecha
print 5 + 8 * 3 + 10

# Si quisieramos hacer primero la suma de la izquierda, deberiamos usar los parentesis
print (5 + 8) * 3 + 10

# Podemos operar numeros enteros y flotantes sin ningun problema
print 5 + 3.2

# Aunque con respecto a la division, Python 2.7 tiene un problema y es que si ninguno de los numeros es flotante,
# el resultado de la division no va a ser flotante
print 5 / 2

# Para ello, hay varias formas
print 5.0 / 2
print 5 / 2.0

# Si se convierte a flotante uno de los numeros o ambos, tambien funciona
print float(5) / 2
print 5 / float(2)
print float(5) / float(2)

# Sin embargo no funciona si intentas convertir el resultado de la operacion
print float(5/2)
# Devuelve un numero flotante, pero no la division que se esperaba

# Si por ejemplo queremos quedarnos con la parte entera de una division (teniendo en cuenta que hemos solucionado el
# problema de la division con decimal), podemos hacerlo de la siguiente manera
print 3.0 // 2

# O podemos quedarnos con el resto de la division usando lo siguiente
print 5 % 2
# Esto es muy util si queremos comprobar que un numero es multiplo de otro

# Si quieres elevar un numero por si mismo n veces, puedes escribirlo n veces
print 2 * 2 * 2 * 2

# O puedes hacerlo de la siguiente manera
print 2 ** 4
# Lo cual simplifica mucho la operacion

# Si queremos obtener la suma de un conjunto de numeros, podemos usar la siguiente funcion
print sum([4, 5, 6])

# Obtener su maximo
print max([4, 5, 3])

# O su minimo
print min([4, 5, 3])

# Existe una libreria en Python, con la cual se pueden realizar operaciones mas complejas
import math

# Raices cuadradas
print math.sqrt(9)

# Potencias (otro modo)
print math.pow(2, 3)
# Y mas tipos de operaciones

