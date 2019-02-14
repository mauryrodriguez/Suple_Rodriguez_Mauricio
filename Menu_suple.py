from tkinter import*
import os
import shutil
import math
import pygame


app=Tk()
app.title('Examen Final - Rodriguez Mauricio')

vp=Frame(app)
vp.grid(column=0, row=0, padx=(100,200), pady=(10,10))
vp.columnconfigure(0,weight=1)
vp.rowconfigure(0,weight=1)


## ------funcion para aplicaciion 1-------
def esfera ():
    radio_esfera=float(input('ingrese el radio de la esfera: '))
    volumen_esfera=(math.pi * radio_esfera**3)/3
    print("El volumen de la esfera es: ", volumen_esfera)

##------funciones para aplicaion 2 --------

def archivos():
    
    nombre = input('Ingrese el nombre del Archivo A crear: ')

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

## -------funciones para aplicacion 3 ----------
def nombre ():
    pygame.init()
    pantalla=pygame.display.set_mode((480,300))
    salir=False
    reloj1=pygame.time.Clock()
    fuente1=pygame.font.Font(None,48)
    texto1=fuente1.render("MAURICIO",0,(255,230,245))

    while salir!=True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir=True

        reloj1.tick(15)
        pantalla.fill((30,30,200))
        pantalla.blit(texto1,(150,200))
        pygame.display.update()
        
    pygame.quit()

##--------salir---------


def fin():
    pygame.init()
    pantalla=pygame.display.set_mode((480,300))
    salir=False
    reloj1=pygame.time.Clock()
    fuente1=pygame.font.Font(None,48)
    texto1=fuente1.render("ADIOS !!!!!",0,(255,230,245))

    while salir!=True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir=True

        reloj1.tick(15)
        pantalla.fill((60,60,200))
        pantalla.blit(texto1,(100,150))
        pygame.display.update()
        
    pygame.quit()

etiqueta=Label(vp,text="Selecciona una opción")
boton= Button (vp,text="1 - Aplicacion 1", command=esfera)
boton.grid(column=1,row=1)
boton= Button (vp,text="2 - Aplicacion 2", command=archivos)
boton.grid(column=1,row=2)
boton= Button (vp,text="3 - Aplicacion 3",command=nombre)
boton.grid(column=1,row=3)
boton= Button (vp,text="3- salir",command=fin)
boton.grid(column=1,row=4)

app.mainloop()
