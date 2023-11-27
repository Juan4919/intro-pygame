import pygame as pg
from figura_class import Rectangulo

#inicializar todos los modulos de pygame, pantallas, objetos, sonidos,teclado,etc
pg.init()
#crear la pantalla o sourface
pantalla = pg.display.set_mode( (800,600) )#definicion de tamaño de pantalla
pg.display.set_caption( "Intro Pygame" )#agregar un titulo a mi ventana

game_over = True

rectangulo1 = Rectangulo(0,300,(185, 36, 183))

rectangulo2 = Rectangulo(0,350)


rectangulo3 = Rectangulo(0,360,(52, 185, 36))

rectangulo1.velocidad(1,1)

rectangulo2.velocidad(2,2)

rectangulo3.velocidad(2,2)

while game_over:

    for eventos in pg.event.get():#capturo todos los eventos mientras se ejecuta el bucle
        print(eventos)
        if eventos.type == pg.QUIT:
            game_over = False

    pantalla.fill( ( 24, 238, 238) )#asignar un color a la pantalla

    rectangulo1.mover()
    rectangulo2.mover()
    rectangulo3.mover()  

    #y= y-1 
    #la pantalla o sourface, color rgb, posiciones(posicionX, posicionY,tamañoX,tamañoY)
    pg.draw.rect( pantalla,rectangulo1.color, (rectangulo1.pos_x,rectangulo1.pos_y,rectangulo1.w,rectangulo1.h) )#dibujando el rectangulo
    pg.draw.rect( pantalla,rectangulo2.color, (rectangulo2.pos_x,rectangulo2.pos_y,rectangulo2.w,rectangulo2.h)  )
    pg.draw.rect( pantalla,rectangulo3.color, (rectangulo3.pos_x,rectangulo3.pos_y,rectangulo3.w,rectangulo3.h)  )

    pg.display.flip()#funcion para cargar toda la configuracion que va dentro de la pantalla

pg.quit()







