from tkinter import *
import math
points=[
    50,50,
    50,150,
    250,150,
    250,50
]
root=Tk()
root.title('Output')
root.geometry("900x700")

can=Canvas(root, width=600, height=400, bg="white")
can.pack(pady=20, expand=True, fill='both', side='right')

sidebar=Frame(root,width=200, bg='#CCC', height=400, relief='sunken', borderwidth=2)
sidebar.pack(expand=True, fill='both', side='left', anchor='nw')

can.create_polygon(points, fill="pink")

def scale():
    sx=0.5
    sy=0.5
    can.delete("all")
    cord=[]
    for i in range(len(points)):
        if(i%2==0):
            cord.append(int(points[i]*sx))
        else:
            cord.append(int(points[i]*sy))
    can.create_polygon(cord, fill="pink")

def shearing():
    # [x', y']=[x,y]*[ 1 ,Shy
    #                  Shx, 1 ]
    Shx=2
    Shy=0
    can.delete("all")
    cord=[]
    for i in range(len(points)):
        if(i%2==0):
            cord.append(int(points[i]+points[i+1]*Shx))
        else:
            cord.append(int(points[i]+points[i-1]*Shy))
    can.create_polygon(cord, fill="pink")

def translate():
    tf=[50,30] #translation factor(DX, DY)
    can.delete("all")
    cord=[]
    for i in range(len(points)):
        if(i%2==0):
            cord.append(int(points[i]+tf[0]))
        else:
            cord.append(int(points[i]+tf[1]))
    can.create_polygon(cord, fill="pink")

def rotatePoint():
    can.delete("all")
    theta = math.radians(45)
    cord=[]
    for i in range(len(points)):
        if(i%2==0):
            cord.append(int(points[i]*math.cos(theta)-points[i+1]*math.sin(theta)))
            cord[i]+=100 # as rotation is along 0,0 to not have -ve values and out of screen stuff
        else:
            cord.append(int(points[i-1]*math.sin(theta)+points[i]*math.cos(theta)))
    
    can.create_polygon(cord, fill="pink")


def reset():
    can.delete("all")
    can.create_polygon(points, fill="pink")


translate=Button(sidebar, text='translate', width=100, command=translate)
translate.pack()
scale=Button(sidebar, text='scale', width=100, command=scale)
scale.pack()
rotate=Button(sidebar, text='rotate', width=100, command=rotatePoint)
rotate.pack()
shear=Button(sidebar, text='shearing', width=100, command=shearing)
shear.pack()
reset=Button(sidebar,text='reset', width=100, command=reset)
reset.pack()

root.mainloop()
