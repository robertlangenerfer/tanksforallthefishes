
from bounding_box import *

class Tank:
    def __init__(self,initX,initY,X,Y,health,fire_rate,speed,name,team,angle):
        self.ix=initX
        self.iy=initY
        self.x=X
        self.y=Y
        self.health=health
        self.fr=fire_rate
        self.speed=speed
        self.name=name
        self.team=team
        self.angle=angle
    box = bounding_box.buildbox(x,y,25,25)
    
    def Tank_collsion(A:bounding_box,B:bounding_box):
        bounding_box.collsion(A,B)


