from bounding_box import *

class Tank:
    def __init__(self,initX,initY,x,y,health,fire_rate,speed,name,team,angle):
        self.ix=initX
        self.iy=initY
        self.x=initX+13
        self.y=initY+13
        self.health=health
        self.fr=fire_rate
        self.speed=speed
        self.name=name
        self.team=team
        self.angle=angle
        self.shape = canvas.create_circle(self, x, y, r, tag=tag)
    box = bounding_box.buildbox(x,y,25,25)
    
    def Tank_collsion(A:bounding_box,B:bounding_box):
        bounding_box.collsion(A,B)
