class Rectangulo:
    def __init__(self,pos_x,pos_y, color=(255,255,255),w=20,h=20):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.w = w
        self.h = h
        self.vx = 0
        self.vy = 0

    def velocidad(self,vx,vy):
        self.vx = vx
        self.vy = vy

    def mover(self):
        self.pos_x += self.vx
        self.pos_y += self.vy
        if self.pos_x == 800 or self.pos_x==0:
            self.vx = self.vx*-1

        if self.pos_y == 600 or self.pos_y == 0:
            self.vy = self.vy*-1






