from turtle import *
from random import randint

scr = Screen()
scr.bgcolor('black')

tur = Turtle()
tur.width(2)
tur.pencolor('red')
tur.shape('turtle')
tur.speed('fastest')

tur.right(90)
tur.forward(100)
tur.circle(100, 180)
tur.forward(100)
tur.left(120)
tur.forward(120)
tur.right(60)
tur.forward(120)

tur.right(150)
tur.penup()
tur.forward(100)
tur.right(60)
tur.pendown()
for x in range(3):
    tur.forward(100)
    tur.right(120)

done()