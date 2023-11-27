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
vy=1

x2=0
y2=500
vx2=1
vy2=1
while game_over:

    for eventos in pg.event.get():#capturo todos los eventos mientras se ejecuta el bucle
        print(eventos)
        if eventos.type == pg.QUIT:
            game_over = False

    pantalla.fill( ( 24, 238, 238) )#asignar un color a la pantalla
    x= x+vx 
    y = y+vy

    x2= x2+vx2 
    y2 = y2+vy2

    if x == 800 or x==0:
        vx = vx*-1

    if y == 600 or y ==0:
        vy = vy*-1

    if x2 == 800 or x2==0:
        vx2 = vx2*-1

    if y2 == 600 or y2 ==0:
        vy2 = vy2*-1    

    #y= y-1 
    #la pantalla o sourface, color rgb, posiciones(posicionX, posicionY,tamañoX,tamañoY)
    pg.draw.rect( pantalla,( 240, 65, 14 ), (x,y,20,20)   )#dibujando el rectangulo
    pg.draw.rect( pantalla,( 185, 90, 36 ), (x2,y2,20,20)   )

    pg.display.flip()#funcion para cargar toda la configuracion que va dentro de la pantalla

pg.quit()







