import pygame as pg
from figura_class import Figura
import random as ra

#inicializar todos los modulos de pygame, pantallas, objetos, sonidos,teclado,etc
pg.init()
#crear la pantalla o sourface
X_MAX = 1000
Y_MAX = 800
pantalla = pg.display.set_mode( (X_MAX,Y_MAX) )#definicion de tamaño de pantalla
pg.display.set_caption( "Intro Pygame" )#agregar un titulo a mi ventana

game_over = True

lista_circulos=[]
lista_rectangulos=[]
for i in range(1,51):
    lista_circulos.append(Figura(ra.randint(0,700), ra.randint(0,500),(ra.randint(0,255),ra.randint(0,255),ra.randint(0,255) ),radio=ra.randint(10,100) ) )
for i in range(1,51):
    lista_rectangulos.append(Figura(ra.randint(0,700), ra.randint(0,500),(ra.randint(0,255),ra.randint(0,255),ra.randint(0,255) ),w=ra.randint(10,100),h=ra.randint(10,100) ) )


while game_over:

    for eventos in pg.event.get():#capturo todos los eventos mientras se ejecuta el bucle
        print(eventos)
        if eventos.type == pg.QUIT:
            game_over = False

    pantalla.fill( ( 24, 238, 238) )#asignar un color a la pantalla

    for circulos in lista_circulos:
        circulos.mover(xmax=X_MAX,ymax=Y_MAX)
        circulos.dibujarCirculo(pantalla)

    for rectangulos in lista_rectangulos:
        rectangulos.mover()
        rectangulos.dibujarRectangulo(pantalla)    

    

    pg.display.flip()#funcion para cargar toda la configuracion que va dentro de la pantalla

pg.quit()







