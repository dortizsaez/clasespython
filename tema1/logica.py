# Una simple prueba de que existe la h en la cadena
h_encontrada = "h" in "hola mundo"
print h_encontrada
# Al existir, el valor almacenado en la variable seria True

# Probemos con una h en mayuscula
h_encontrada = "h" in "Hola Mundo"
print h_encontrada
# Python es case sensitive, lo que quiere decir que diferencia mayusculas de minusculas, por eso devuelve False

# Si probamos comprobaciones de mayor que o menor que, vemos que tambien nos devuelve True o False dependiendo de la
# comprobacion
a = 5
b = 6

es_mayor = b > a
print es_mayor

es_menor = a < b
print es_menor

# Tambien podemos concatenar distintos valores booleanos usando and, or
concatenacion = "h" in "hola mundo" and es_mayor
print concatenacion

# Si utilizamos and, sus valores en ambos lados debe de ser True, por que si no devuelve un False
resultado = True and False
print resultado
# Como se puede ver, el resultado es False ya que no ha cumplido la condicion

# Sin embargo, al utilizar or, con que alguno tenga valor True es suficiente para que se cumpla
resultado = True or False
print resultado

# El operador not lo que hace es invertir el valor del booleano, como se puede ver
afirmativo = not True
print afirmativo
