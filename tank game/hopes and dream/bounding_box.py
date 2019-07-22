class location:
    def __init__(self,x:int,y:int):
        self.x=x
        self.y=y

class bounding_box: #class for bounding box
   
    def __init__(self,max:location,min:location):
       self.max=max
       self.min=min
    def buildbox(x,y,width,height):  #function to build the box
        max=(x+(width/2),y-(height/2))
        min=(x-(width/2),y+(height/2))
        box=(max,min)
        return box 
    def collsion(A,B):
       
        return not ((A.max.x < B.min.x) or (B.max.x <A.min.x) or (A.max.y<B.min.y) or (B.max.y<A.min.y))

        





