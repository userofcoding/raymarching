from tkinter import *
from math import *

root = Tk()
 
C = Canvas(root, bg="black",
           height=360, width=480)

class vc:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def norm():
        m = sqrt(self.x*self.x + self.y*self.y + self.z*self.z)
        self.x = self.x/m
        self.y = self.y/m
        self.z = self.z/m

cm = vc(0,0,0)

def length(v):
    tv = vc(v[0],v[1],v[2])
    return sqrt(tv.x*tv.x + tv.y*tv.y + tv.z*tv.z)

def dstFromSphere(c_, p, radius):
    c = vc(c_[0],c_[1],c_[2])
    centerminp = [c.x-p.x,c.y-p.y,c.z-p.z]
    return length(centerminp) - radius

def dstFromCube(c_, p, size):
    # super confusing. don't even try to understand this, future me.
    c = vc(c_[0],c_[1],c_[2])
    pmincenter = [p.x-c.x,p.y-c.y,p.z-c.z]
    pmcab = [abs(pmincenter[0]),abs(pmincenter[1]),abs(pmincenter[2])]
    offset = [pmcab[0]-size,pmcab[1]-size,pmcab[2]-size]
    unsigneddst = length([max(offset[0], 0),max(offset[1], 0),max(offset[2], 0)])
    dstinsidebox = max(min(offset[0],0),min(offset[1],0),min(offset[2],0))
    return unsigneddst+dstinsidebox


def dstFromScene(cam):
    dst = min(dstFromSphere([5,0,0],cam,1), dstFromCube([5,0,2],cam,1), dstFromCube([-6,0,0],cam,2))
    
    return dst

def normalize(v):
    m = length([v.x,v.y,v.z])
    return [v.x/m,v.y/m,v.z/m]

screenwidth = 120
screenheight = 90

def rayGo():
    ray = vc(cm.x,cm.y,cm.z)
    i=10
    screen="""a"""
    for z in range(1,screenwidth):
        for y in range(1,screenheight):
            i=9
            ray.z=(z-(screenwidth/2))/100
            ray.y=(y-(screenheight/2))/100
            ray.x=0.2
            m = sqrt(ray.x*ray.x + ray.y*ray.y + ray.z*ray.z)
            ray.x = ray.x/m
            ray.y = ray.y/m
            ray.z = ray.z/m
            #print(ray.x,ray.y,ray.z)
            while i>0:
                #print(length([ray.x,ray.y,ray.z]))
                ray.x += ray.x*dstFromScene(ray)
                ray.y += ray.y*dstFromScene(ray)
                ray.z += ray.z*dstFromScene(ray)
                #print(ray.x,ray.y,ray.z)
                #print(dstFromScene(ray))
                if dstFromScene(ray) < 0.1:
                    screen=screen+"#"
                    C.create_rectangle((z*4)-3,(y*4)-3,z*4,y*4,fill="white",outline="white")
                else:
                    screen=screen+"("
                i-=1
        screen+="\n"
    #print(screen)
                
rayGo()

"""def movL(speed):
    cm.z-=speed
    rayGo()
def movR(speed):
    cm.z+=speed
    rayGo()
def movF(speed):
    cm.x+=speed
    rayGo()
def movB(speed):
    cm.x-=speed
    rayGo()
def movU(speed):
    cm.y+=speed
    rayGo()
def movD(speed):
    cm.y-=speed
    rayGo()
root.bind("w",movF(0.1))
root.bind("s",movB(0.1))
root.bind("a",movL(0.1))
root.bind("d",movR(0.1))
root.bind("<Space>",movU(0.1))
root.bind("<Down>",movD(0.1))"""

C.pack()
mainloop()
