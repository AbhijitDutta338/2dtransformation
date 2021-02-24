import math
# points =[x1,y1,x2,y2,....] points in polygon
# cord[] in functions is the new coordinates of corners in polygon
points=[
    50,50,
    50,150,
    250,150,
    250,50
]
def scale():
    sx=0.5
    sy=0.5
    cord=[]
    for i in range(len(points)):
        if(i%2==0):
            cord.append(int(points[i]*sx))
        else:
            cord.append(int(points[i]*sy))

def shearing():
    # [x', y']=[x,y]*[ 1 ,Shy
    #                  Shx, 1 ]
    Shx=2
    Shy=0
    cord=[]
    for i in range(len(points)):
        if(i%2==0):
            cord.append(int(points[i]+points[i+1]*Shx))
        else:
            cord.append(int(points[i]+points[i-1]*Shy))

def translate():
    tf=[50,30] #translation factor(DX, DY)
    cord=[] 
    for i in range(len(points)):
        if(i%2==0):
            cord.append(int(points[i]+tf[0]))
        else:
            cord.append(int(points[i]+tf[1]))

def rotatePoint():
    theta = math.radians(45)
    cord=[]
    for i in range(len(points)):
        if(i%2==0):
            cord.append(int(points[i]*math.cos(theta)-points[i+1]*math.sin(theta)))
        else:
            cord.append(int(points[i-1]*math.sin(theta)+points[i]*math.cos(theta)))
    
