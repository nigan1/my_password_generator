import random

#agregar en la lista todas las palabras claves que quieras incluir en tu contraseña(asi la puedes memorizar y evitar las contraseñas generadas
#automaticamente que no tiene nada que ver con la persona y cuya unica forma de usar seria teniendolas en almacenamiento)
#mientras mas agregues mejor, recuerda agregar caracteres especiales, mayusculas y numeros

password=["@merica",1992,2564,"Alberto","python"]

#el numero es la cantidad de elementos de la lista a escoger para la contraseña,a mayor seea, mas seguro

a=random.sample(password,4)

str="".join(map(str,a))

print(str)
    