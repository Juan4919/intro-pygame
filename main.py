import pygame as pg
from figura_class import Rectangulo,Circulo

#inicializar todos los modulos de pygame, pantallas, objetos, sonidos,teclado,etc
pg.init()
#crear la pantalla o sourface
pantalla = pg.display.set_mode( (800,600) )#definicion de tamaño de pantalla
pg.display.set_caption( "Intro Pygame" )#agregar un titulo a mi ventana

game_over = True
"""
rectangulo1 = Rectangulo(0,300,(185, 36, 183))
rectangulo2 = Rectangulo(0,350,vx=2,vy=2)
rectangulo3 = Rectangulo(0,360,(52, 185, 36))
"""

circulo1 = Circulo(0,300)
circulo2 = Circulo(0,360,( 95, 10, 72 ),vx=2,vy=2)
circulo3 = Circulo(0,500,( 251, 244, 8),20,2,2)

while game_over:

    for eventos in pg.event.get():#capturo todos los eventos mientras se ejecuta el bucle
        print(eventos)
        if eventos.type == pg.QUIT:
            game_over = False

    pantalla.fill( ( 24, 238, 238) )#asignar un color a la pantalla

    """
    rectangulo1.mover()
    rectangulo2.mover()
    rectangulo3.mover()  

    rectangulo1.dibujar(pantalla)
    rectangulo2.dibujar(pantalla)
    rectangulo3.dibujar(pantalla)
    """
    circulo1.mover()
    circulo2.mover()
    circulo3.mover()

    circulo1.dibujar(pantalla)
    circulo2.dibujar(pantalla)
    circulo3.dibujar(pantalla)

    pg.display.flip()#funcion para cargar toda la configuracion que va dentro de la pantalla

pg.quit()







