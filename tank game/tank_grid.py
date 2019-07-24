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
    def __init__(self,tag,initX,initY,x,y,width,height,speed):
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
        
    def update(self): # calls the check_Wall_Collision to update the ball's place
        canvas.move(self.shape,self.x,self.y)
        self.check_Wall_Collision()
  
   def check_Wall_Collision(self):
       # checks for wall collision
       canvas.move(self.shape, self.vx, self.vy)
       x1=box.x-box.width/2
       y1=box.y-box.height/2
       x2=box.x+box.width/2
       y2=box.y+box.height/2
       if x2 >=self.width or x1 <= 0:

           self.vx *= -1
       if y2 >= self.height or y1 <= 0:
           self.vy *= -1
  

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
def cycle():
       # cycles the program
       canvas.tag_raise("bg")
       tank.update()
       canvas.tag_raise("tank")
       tank_2.update()
       canvas.tag_raise("tank_2")
       tk.update_idletasks()
       tk.after(3, cycle) 
tank = Tank("tank",5,5,100,50,30,30,1)
tank_2 = Tank("tank_2",405,405,400,450,30,30,1)
tk.after(0, cycle)



tk.mainloop()
