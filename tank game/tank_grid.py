from tkinter import *
from tank import *
from bounding_box import *
# creates a vanvas for the size of the board
WIDTH=500
HEIGHT=500
tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT, bg="blue")
canvas.pack()

x1 = 0
x2 = 500
class Tank:
    def __init__(self,initX,initY,x,y,width,height,speed):
        self.ix=initX
        self.iy=initY
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.point= [self.x- self.width/8,  self.y-self.height/2,          
                     self.x + self.width/8,  self.y-self.height/2,           
                     self.x + self.width/8,  self.y,             
                     self.x + self.width/2,  self.y,       
                     self.x + self.width/2,   self.y+self.height/2,       
                     self.x -self.width/2,    self.y+self.height/2,
                     self.x - self.width/2,    self.y, 
                     self.x -self.width/8,     self.y
                     ]
  
        self.box=bounding_box(self.x,self.y,self.width,self.height)
        self.shape =  canvas.create_polygon(self.point,fill="green", tags="bg")
        

    
    def Tank_collsion(A:bounding_box,B:bounding_box):
        bounding_box.collsion(A,B)
# Both for statements creates the grid on the canvas
for k in range(0, 500, 25):
    y1 = k
    y2 = k
    canvas.create_line(x1, y1, x2, y2)

y1 = 0
y2 = 500
for k in range(0, 500,25):
    x1 = k
    x2 = k
    canvas.create_line(x1, y1, x2, y2)

 #  (50, 25, 25, 50, ) (postion for x, size x, size y, postion for y)   when size x changes postion y changes and when postion x changes size y changes.  
 # postion for x must be 25 greater size y
 # postion for y must be 25 greater size x
tank = Tank(5,5,100,50,30,30,1)


tk.mainloop()
