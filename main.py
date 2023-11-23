import pygame as pg

#inicializar todos los modulos de pygame, pantallas, objetos, sonidos,teclado,etc
pg.init()


#crear la pantalla o sourface
pantalla = pg.display.set_mode( (800,600) )#definicion de tamaño de pantalla
pg.display.set_caption( "Intro Pygame" )#agregar un titulo a mi ventana

game_over = True
x=0
y=300
vx=1
while game_over:

    for eventos in pg.event.get():#capturo todos los eventos mientras se ejecuta el bucle
        print(eventos)
        if eventos.type == pg.QUIT:
            game_over = False

    pantalla.fill( ( 24, 238, 238) )#asignar un color a la pantalla
    x= x+vx 

    if x == 800 or x==0:
        vx = vx*-1
    #y= y-1 
    #la pantalla o sourface, color rgb, posiciones(posicionX, posicionY,tamañoX,tamañoY)
    pg.draw.rect( pantalla,( 240, 65, 14 ), (x,y,20,20)   )#dibujando el rectangulo



    pg.display.flip()#funcion para cargar toda la configuracion que va dentro de la pantalla

pg.quit()







