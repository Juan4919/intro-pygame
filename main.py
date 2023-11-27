import pygame as pg
from figura_class import Figura

#inicializar todos los modulos de pygame, pantallas, objetos, sonidos,teclado,etc
pg.init()
#crear la pantalla o sourface
pantalla = pg.display.set_mode( (800,600) )#definicion de tamaño de pantalla
pg.display.set_caption( "Intro Pygame" )#agregar un titulo a mi ventana

game_over = True

rectangulo1 =  Figura(0,345,(185, 36, 183))
rectangulo2 = Figura(0,200,vx=2,vy=2,w=25,h=25)
rectangulo3 = Figura(0,150,(52, 185, 36))


circulo1 = Figura(0,300)
circulo2 = Figura(0,360,( 95, 10, 72 ),radio=15,vx=2,vy=2)
circulo3 = Figura(0,500,( 251, 244, 8),radio=20,vx=2,vy=2)

while game_over:

    for eventos in pg.event.get():#capturo todos los eventos mientras se ejecuta el bucle
        print(eventos)
        if eventos.type == pg.QUIT:
            game_over = False

    pantalla.fill( ( 24, 238, 238) )#asignar un color a la pantalla

    
    rectangulo1.mover()
    rectangulo2.mover()
    rectangulo3.mover()  

    rectangulo1.dibujarRectangulo(pantalla)
    rectangulo2.dibujarRectangulo(pantalla)
    rectangulo3.dibujarRectangulo(pantalla)
    
    circulo1.mover()
    circulo2.mover()
    circulo3.mover()

    circulo1.dibujarCirculo(pantalla)
    circulo2.dibujarCirculo(pantalla)
    circulo3.dibujarCirculo(pantalla)

    pg.display.flip()#funcion para cargar toda la configuracion que va dentro de la pantalla

pg.quit()







