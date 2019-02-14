import os
import shutil

print("Copia de Archivos")
nombre = input("Ingrese El Nombre Del Archivo  [ A ]: ")

def creartxt():

    txt = open(nombre + '.txt', 'w')
    txt.close()

def guardartxt():

    txt = open(nombre + '.txt', 'a')
    txt.write(input('Ingrese El Texto: '))
    txt.close()

def leertxt():

    txt = open(nombre + '.txt', 'r')
    contenido = txt.readline()
    while  contenido != "":
        print(contenido)
        contenido = txt.readline()
    txt.close()

creartxt()
guardartxt()
leertxt()


def copiararchivo():

    ruta = os.getcwd() + os.sep
    origen = ruta + nombre + '.txt'
    destino = ruta + 'Copia ' + nombre + '.txt'

    if os.path.exists(origen):
        with open(origen, 'rb') as forigen:
            with open(destino, 'wb') as fdestino:
                shutil.copyfileobj(forigen, fdestino)
copiararchivo()
